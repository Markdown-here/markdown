"""Render every Mermaid diagram in media/ to SVG, in the course colors.

    python scripts/render_media.py          # render .mmd files whose .svg is missing or older
    python scripts/render_media.py --all    # render all of them
    python scripts/render_media.py --check  # fail if any .svg is missing or older than its .mmd

Each media/<name>.mmd becomes media/<name>.svg. Commit both: the .mmd is the source,
the .svg is what slides and GitHub show. Colors come from media/mermaid.json.

Needs `npm install` first (it uses @mermaid-js/mermaid-cli). It drives a browser:
set CHROME_PATH to use one you already have, such as Edge on Windows:
    set CHROME_PATH=C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEDIA = ROOT / "media"
CONFIG = MEDIA / "mermaid.json"


def stale(mmd):
    svg = mmd.with_suffix(".svg")
    return not svg.exists() or svg.stat().st_mtime < mmd.stat().st_mtime


def render(mmd, puppeteer_config):
    svg = mmd.with_suffix(".svg")
    cmd = ["npx", "--no-install", "mmdc", "-i", str(mmd), "-o", str(svg),
           "-c", str(CONFIG), "-b", "transparent", "--svgId", mmd.stem, "-q"]
    if puppeteer_config:
        cmd += ["-p", puppeteer_config]
    result = subprocess.run(cmd, cwd=ROOT, shell=(os.name == "nt"), capture_output=True, text=True)
    if result.returncode:
        print(f"ERROR {mmd.relative_to(ROOT)}:\n{result.stderr.strip()}", file=sys.stderr)
        return False
    print(f"rendered {svg.relative_to(ROOT)}")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--all", action="store_true", help="render every diagram, not just changed ones")
    ap.add_argument("--check", action="store_true", help="only report diagrams whose SVG is missing or out of date")
    args = ap.parse_args()

    diagrams = sorted(MEDIA.glob("*.mmd"))
    todo = diagrams if args.all else [m for m in diagrams if stale(m)]

    if args.check:
        for m in todo:
            print(f"out of date: {m.relative_to(ROOT)}", file=sys.stderr)
        print(f"OK: {len(diagrams)} diagrams" if not todo else f"{len(todo)} diagram(s) need rendering")
        return 1 if todo else 0

    if not todo:
        print(f"OK: {len(diagrams)} diagrams, all up to date")
        return 0

    puppeteer_config = None
    if os.environ.get("CHROME_PATH"):
        f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump({"executablePath": os.environ["CHROME_PATH"], "args": ["--no-sandbox"]}, f)
        f.close()
        puppeteer_config = f.name

    ok = all([render(m, puppeteer_config) for m in todo])
    if puppeteer_config:
        os.unlink(puppeteer_config)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

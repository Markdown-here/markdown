"""Stamp a version into the footer of every deck and Marp file before a build.

    python scripts/stamp_version.py v0.1

Turns `footer: "Markdown 101 · ..."` into `footer: "Markdown 101 · v0.1 · ..."`.
Run it in CI only: it edits files in place and the result isn't meant to be committed.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOOTER = re.compile(r'^(\s*footer: "Markdown 101)( ·)', re.M)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    version = sys.argv[1]
    stamped = 0
    files = list((ROOT / "course").rglob("*.md")) + list((ROOT / "course").rglob("*.yml"))
    for p in sorted(files):
        text = p.read_text(encoding="utf-8")
        new, n = FOOTER.subn(rf"\1 · {version}\2", text, count=1)
        if n:
            p.write_text(new, encoding="utf-8", newline="\n")
            stamped += 1
            print(f"stamped {p.relative_to(ROOT)}")
    if not stamped:
        sys.exit("No footers found to stamp")


if __name__ == "__main__":
    main()

"""Stamp a version into the footer of every Marp file before a build.

    python scripts/stamp_version.py v1.0.0

Turns `footer: "Markdown 101 · ..."` into `footer: "Markdown 101 v1.0.0 · ..."`.
Run it in CI only: it edits files in place and the result isn't meant to be committed.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOOTER = re.compile(r'^(footer: "Markdown 101)( ·)', re.M)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    version = sys.argv[1]
    stamped = 0
    for p in sorted((ROOT / "course").rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        new, n = FOOTER.subn(rf"\1 {version}\2", text, count=1)
        if n:
            p.write_text(new, encoding="utf-8", newline="\n")
            stamped += 1
            print(f"stamped {p.relative_to(ROOT)}")
    if not stamped:
        sys.exit("No footers found to stamp")


if __name__ == "__main__":
    main()

"""Check that every link inside the built website points at a page that exists.

    python scripts/check_site_links.py public

Run it after `hugo` has built the site into `public/`. Links to other websites
aren't checked here; the weekly Links workflow does that for the source files.
"""
import html
import re
import sys
from pathlib import Path

HREF = re.compile(r'(?:href|src)="([^"]+)"')
SKIP = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//|#)", re.I)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = Path(sys.argv[1]).resolve()
    if not (root / "index.html").is_file():
        sys.exit(f"{root} has no index.html. Build the site first: hugo")
    broken = set()
    pages = sorted(root.rglob("*.html"))
    for page in pages:
        for href in HREF.findall(page.read_text(encoding="utf-8")):
            href = html.unescape(href)
            if SKIP.match(href):
                continue
            path = href.split("#")[0].split("?")[0]
            if not path:
                continue
            target = root / path.lstrip("/") if path.startswith("/") else page.parent / path
            if not (target.is_file() or (target / "index.html").is_file()):
                broken.add((str(page.relative_to(root)), href))
    for page, href in sorted(broken):
        print(f"{page}: broken link {href}")
    if broken:
        sys.exit(f"{len(broken)} broken links")
    print(f"OK: {len(pages)} pages, no broken links")


if __name__ == "__main__":
    main()

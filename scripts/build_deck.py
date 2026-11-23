"""Assemble a Marp deck from one-slide Markdown files.

    python scripts/build_deck.py course/markdown-101/deck.yml
    python scripts/build_deck.py course/markdown-101/editions/microsoft-deck.yml --list
    python scripts/build_deck.py course/markdown-101/editions/microsoft-deck.yml --check

A deck file (YAML) lists slides by ID. An ID is a slide's file name without `.md`.

    type: Deck
    output: markdown-101             # writes dist/markdown-101.md
    frontmatter: {marp: true, ...}   # Marp settings for the whole deck
    slide_dirs: [slides]             # where to find slide files
    slides: [title, hook, ...]       # the order

A deck can extend another one and change it:

    extends: ../deck.yml
    slide_dirs: [microsoft-slides]   # searched first, so a file here with the
                                     # same name as a base slide replaces it
    insert:
      - after: hook                  # or before:
        slides: [what-copilot-sends]
    remove: [some-slide]

Paths are relative to the deck file that names them. Links and images in a slide
are relative to the slide file; they're rewritten to work from the output folder.
"""
import argparse
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DIST = Path("dist")  # relative to where you run the script
FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
CODE_SPAN_RE = re.compile(r"(`+)(?:.+?)\1")
LINK_RE = re.compile(r"(\]\()([^)\s]+)")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


class DeckError(Exception):
    pass


def load(path, seen=()):
    """Return the resolved deck: frontmatter, slide dirs, slide IDs, output name."""
    path = Path(path).resolve()
    if path in seen:
        raise DeckError(f"{rel(path)}: `extends` loops back on itself")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if data.get("type") != "Deck":
        raise DeckError(f"{rel(path)}: first field must be `type: Deck`")

    if data.get("extends"):
        base = load(path.parent / data["extends"], seen + (path,))
    else:
        base = {"frontmatter": {}, "slide_dirs": [], "slides": [], "output": None}

    dirs = [path.parent / d for d in data.get("slide_dirs", [])] + base["slide_dirs"]
    slides = list(data["slides"]) if "slides" in data else list(base["slides"])

    for rid in data.get("remove", []) or []:
        if rid not in slides:
            raise DeckError(f"{rel(path)}: can't remove `{rid}`, it isn't in the deck")
        slides.remove(rid)

    for ins in data.get("insert", []) or []:
        anchor = ins.get("after") or ins.get("before")
        if anchor not in slides:
            raise DeckError(f"{rel(path)}: can't insert next to `{anchor}`, it isn't in the deck")
        i = slides.index(anchor) + (1 if "after" in ins else 0)
        slides[i:i] = ins["slides"]

    return {
        "frontmatter": {**base["frontmatter"], **(data.get("frontmatter") or {})},
        "slide_dirs": dirs,
        "slides": slides,
        "output": data.get("output") or base["output"],
        "path": path,
    }


def rel(p):
    """Show a path relative to where the script runs, or to the repo."""
    p = Path(p).resolve()
    for base in (Path.cwd().resolve(), ROOT):
        try:
            return p.relative_to(base).as_posix()
        except ValueError:
            pass
    return str(p)


def find(slide_id, dirs):
    for d in dirs:
        p = d / f"{slide_id}.md"
        if p.is_file():
            return p
    raise DeckError(f"slide `{slide_id}` not found in: {', '.join(rel(d) for d in dirs)}")


def outside_code(lines):
    """Yield (index, is_code) for each line, tracking fenced code blocks."""
    fence = None
    for i, line in enumerate(lines):
        m = FENCE_RE.match(line)
        if fence:
            yield i, True
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not line.strip()[len(m.group(1)):].strip():
                fence = None
        elif m:
            fence = m.group(1)
            yield i, True
        else:
            yield i, False


def read_slide(path, out_dir):
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    fm = yaml.safe_load(m.group(1)) if m else None
    if not fm or list(fm)[0] != "type" or fm["type"] != "Slide":
        raise DeckError(f"{rel(path)}: must start with frontmatter `type: Slide`")
    body = text[m.end():].strip("\n")

    lines = body.split("\n")
    for i, is_code in outside_code(lines):
        if is_code:
            continue
        if lines[i].strip() == "---":
            raise DeckError(f"{rel(path)}: one slide per file, but line {i + 1} is a slide break `---`")
        lines[i] = rewrite_links(lines[i], path.parent, out_dir)
    return "\n".join(lines)


def rewrite_links(line, src_dir, out_dir):
    """Make relative link and image targets work from out_dir. Leaves code spans alone."""
    parts, last = [], 0
    for m in CODE_SPAN_RE.finditer(line):
        parts.append((line[last:m.start()], True))
        parts.append((m.group(0), False))
        last = m.end()
    parts.append((line[last:], True))

    def fix(m):
        target = m.group(2)
        if SCHEME_RE.match(target) or target.startswith(("#", "/")):
            return m.group(0)
        new = os.path.relpath((src_dir / target).resolve(), out_dir.resolve())
        return m.group(1) + Path(new).as_posix()

    return "".join(LINK_RE.sub(fix, text) if rewrite else text for text, rewrite in parts)


def build(deck_path, out_dir=DIST):
    deck = load(deck_path)
    if not deck["output"]:
        raise DeckError(f"{rel(deck_path)}: needs an `output` name")
    if len(set(deck["slides"])) != len(deck["slides"]):
        dupes = sorted({s for s in deck["slides"] if deck["slides"].count(s) > 1})
        raise DeckError(f"{rel(deck_path)}: slides appear twice: {', '.join(dupes)}")

    sources = [find(s, deck["slide_dirs"]) for s in deck["slides"]]
    bodies = [read_slide(p, out_dir) for p in sources]

    fm = {"type": "Presentation", **{k: v for k, v in deck["frontmatter"].items() if k != "type"}}
    header = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000)
    note = f"<!-- Built by scripts/build_deck.py from {rel(deck['path'])}. Edit the slide files, not this one. -->"
    text = f"---\n{header}---\n\n{note}\n\n" + "\n\n---\n\n".join(bodies) + "\n"
    return deck, sources, out_dir / f"{deck['output']}.md", text


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("decks", nargs="+", help="deck YAML files")
    ap.add_argument("-o", "--out-dir", default=str(DIST), help="output folder (default: dist/)")
    ap.add_argument("--check", action="store_true", help="validate only, write nothing")
    ap.add_argument("--list", action="store_true", help="print the slide order and where each slide comes from")
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    failed = False
    for d in args.decks:
        try:
            deck, sources, out, text = build(d, out_dir)
        except DeckError as e:
            print(f"ERROR {e}", file=sys.stderr)
            failed = True
            continue
        if args.list:
            for n, (sid, src) in enumerate(zip(deck["slides"], sources), 1):
                print(f"{n:3}  {sid:28} {rel(src.parent)}")
        if not args.check:
            out_dir.mkdir(parents=True, exist_ok=True)
            out.write_text(text, encoding="utf-8", newline="\n")
        print(f"OK: {rel(d)}: {len(sources)} slides" + ("" if args.check else f" -> {rel(out)}"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

---
type: Guide
---

# Extending Markdown 101

The deck is built from one Markdown file per slide. A short deck file lists which slides to use and in what order. That makes it easy to add, replace, or drop slides without editing the originals, so your copy keeps getting updates from this repo.

## How a deck is built

| Path | What |
|:---|:---|
| [`slides/`](slides/) | The core slides, one per file. The file name is the slide's ID, like `headings` |
| [`deck.yml`](deck.yml) | The core deck: Marp settings and the slide order |
| [`editions/microsoft-slides/`](editions/microsoft-slides/) | Microsoft edition slides |
| [`editions/microsoft-deck.yml`](editions/microsoft-deck.yml) | The Microsoft edition: the core deck plus changes |

[`scripts/build_deck.py`](../../scripts/build_deck.py) joins the slides into one Marp file in `dist/`:

```bash
python scripts/build_deck.py course/markdown-101/editions/microsoft-deck.yml --list
```

`--list` prints each slide and the folder it came from. Open the result, `dist/markdown-101-microsoft.md`, in VS Code to preview it with Marp. `npm run build` builds every deck and exports HTML, PDF, and PowerPoint.

## A slide file

```markdown
---
type: Slide
---

## Headings

...
```

- One slide per file. No `---` slide breaks outside code blocks.
- Marp comments like `<!-- _class: lead -->` and speaker notes `<!-- ... -->` go in the slide file.
- Link images relative to the slide file, for example `../../../media/diagram.svg`. The build fixes the paths.
- **Slide IDs are permanent.** Other decks point at them. Don't rename one; add a new slide instead.

## Make your own edition

A deck file can start from another deck and change it:

```yaml
type: Deck
output: markdown-101-acme          # builds dist/markdown-101-acme.md
extends: ../deck.yml               # or editions/microsoft-deck.yml
frontmatter:
  description: Markdown 101 for Acme
slide_dirs: [acme-slides]          # searched first
insert:
  - after: tables
    slides: [acme-wiki]            # acme-slides/acme-wiki.md
  - before: closing
    slides: [acme-style-guide]
remove: [diagrams]
```

| To | Do this |
|:---|:---|
| Add a slide | Put the file in your slide folder and list it under `insert` with `after:` or `before:` |
| Replace a slide | Put a file **with the same name** in your slide folder, like `acme-slides/hook.md` |
| Drop a slide | List its ID under `remove` |
| Change settings | Add keys under `frontmatter`, like `footer` or `theme`. They override the base deck |

The build stops with an error if a deck points at a slide that doesn't exist. That way, if this repo renames or removes something, you find out at build time, not in front of an audience.

## Keep a private copy

GitHub doesn't allow a private fork of a public repo. Make a new private repo and bring this one in as a submodule, so your slides and ours stay separate:

```bash
git submodule add https://github.com/Markdown-here/markdown upstream
```

```text
acme-markdown-101/            (your private repo)
  upstream/                   this repo, never edited
  acme-slides/
    acme-wiki.md
    hook.md                   replaces the core hook slide
  acme-deck.yml               extends: upstream/course/markdown-101/editions/microsoft-deck.yml
  design/acme.css             optional: @import 'markdown101'; then your colors
```

Build from your repo's root:

```bash
python upstream/scripts/build_deck.py acme-deck.yml
npx @marp-team/marp-cli --theme-set upstream/design --no-stdin dist/markdown-101-acme.md --pdf
```

In VS Code, add the theme to your repo's `.vscode/settings.json`: `"markdown.marp.themes": ["./upstream/design/markdown101.css"]`.

To pick up our updates, move the submodule to a newer release:

```bash
cd upstream
git fetch --tags
git checkout v0.2
```

Pin a release tag rather than `main`, so the course doesn't change under you the week of a session.

Please keep the credit to this repo in the footer.

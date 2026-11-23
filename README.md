---
type: Readme
---

# Markdown

The ultimate Markdown reference: learn it, try it, find everything else worth knowing about it.

AI-first, human-gorgeous. Everything here is plain Markdown with stable IDs, so it reads well on GitHub, renders beautifully on the site, and is trivially consumable by LLMs and agents.

## What's here

| Path | What |
|:---|:---|
| [BRAINSTORM.md](BRAINSTORM.md) | The big idea list: site sections, AI-first features, roadmap |
| [course/markdown-101/](course/markdown-101/) | 30-minute Markdown 101 course (first deliverable) |
| [references/](references/) | The curated reference lists: Resources, Tools, People, Organizations |
| [templates/](templates/) | Entry templates, based on [HAL_md](https://github.com/thephm/hal_md) |
| [work/](work/) | Work-specific context: tools, constraints, docs-as-code to Confluence plan |
| [design/](design/) | One look for slides and handouts: the Marp theme and how to export PDFs |
| [media/](media/) | Source images for slides and handouts |
| [scripts/](scripts/) | `build_references.py`: checks every entry, generates the lists and `references.json` |

## Releases

The course is built into PDF, HTML, and PowerPoint by the [Course workflow](.github/workflows/course.yml). Generated files are never committed.

| When | What you get | Footer says |
|:---|:---|:---|
| Every push to `main` | The `markdown-101` artifact on the workflow run | `Markdown 101 · dev-<commit>` |
| A version tag, like `v0.1` | A [GitHub Release](https://github.com/thephm/markdown/releases) with all files attached | `Markdown 101 · v0.1` |

To release a version:

```bash
git tag v0.1
git push origin v0.1
```

Versions have two parts, `v<major>.<minor>`: bump the major number for a restructured course and the minor number for everything else, like new slides, sections, or fixes. Stay on `v0.x` until the course is ready to call 1.0.

To build locally: `npm install`, then `npm run build`. Files land in `dist/`. After editing a diagram in `media/`, run `npm run media` to update its SVG.

## Document types

Every Markdown file in this repo starts with YAML frontmatter, and its **first field is `type`** (the OKF convention from [HAL_md](https://github.com/thephm/hal_md)). We define the types, always with a capital first letter. The build fails if a file is missing `type` or uses one that isn't listed.

| Type | Used for |
|:---|:---|
| `Readme` | A folder's `README.md` |
| `Instructions` | Instructions for AI agents, like `CLAUDE.md` |
| `Brainstorm` | Idea lists |
| `Course` | A course or course edition |
| `Presentation` | A slide deck ([Marp](references/tools/marp.md)) |
| `Slide` | One slide. Decks are built from these: see [Extending Markdown 101](course/markdown-101/extending.md) |
| `Guide` | How-to instructions |
| `List` | A generated list of references |
| `Inbox` | Items waiting for triage |
| `Context` | Background on an environment, like [work/](work/) |
| `Exercise` | A course exercise: starter file or answer key |
| `Cheatsheet` | A one-page handout |
| `Reference` | A lookup page, like [what works where](work/markdown-support.md) |

Reference entries and templates use their own types (`Resource`, `App`, `Person`, and so on): see [references/README.md](references/README.md). To add a new type, add it here and to `DOC_TYPES` in [`scripts/build_references.py`](scripts/build_references.py).

## Reference IDs

Every reference is its own Markdown file with YAML frontmatter. Its `slug` is the permanent unique ID, and `<section>/<slug>` is its deep link, e.g. [`tools/pandoc`](references/tools/pandoc.md). See [references/README.md](references/README.md) for the full schema.

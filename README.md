---
type: Readme
---

# Markdown

The ultimate Markdown reference: learn it, try it, find everything else worth knowing about it.

AI-first, human-gorgeous. Everything here is plain Markdown with stable IDs, so it reads well on GitHub, renders beautifully on the site, and is trivially consumable by LLMs and agents.

## What's here

| Path | What |
|:---|:---|
| [BRAINSTORM.md](BRAINSTORM.md) | The big idea list — site sections, AI-first features, roadmap |
| [course/markdown-101/](course/markdown-101/) | 30-minute Markdown 101 course (first deliverable) |
| [references/](references/) | The curated reference lists: Resources, Tools, People, Organizations |
| [templates/](templates/) | Entry templates, based on [HAL_md](https://github.com/thephm/hal_md) |
| [work/](work/) | Work-specific context: tools, constraints, docs-as-code to Confluence plan |
| [scripts/](scripts/) | `build_references.py`: checks every entry, generates the lists and `references.json` |

## Document types

Every Markdown file in this repo starts with YAML frontmatter, and its **first field is `type`** (the OKF convention from [HAL_md](https://github.com/thephm/hal_md)). We define the types, always with a capital first letter. The build fails if a file is missing `type` or uses one that isn't listed.

| Type | Used for |
|:---|:---|
| `Readme` | A folder's `README.md` |
| `Instructions` | Instructions for AI agents, like `CLAUDE.md` |
| `Brainstorm` | Idea lists |
| `Course` | A course or course edition |
| `Presentation` | A slide deck ([Marp](references/tools/marp.md)) |
| `List` | A generated list of references |
| `Inbox` | Items waiting for triage |
| `Context` | Background on an environment, like [work/](work/) |

Reference entries and templates use their own types (`Resource`, `App`, `Person`, and so on): see [references/README.md](references/README.md). To add a new type, add it here and to `DOC_TYPES` in [`scripts/build_references.py`](scripts/build_references.py).

## Reference IDs

Every reference is its own Markdown file with YAML frontmatter. Its `slug` is the permanent unique ID, and `<section>/<slug>` is its deep link, e.g. [`tools/pandoc`](references/tools/pandoc.md). See [references/README.md](references/README.md) for the full schema.

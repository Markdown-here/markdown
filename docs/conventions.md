---
type: Reference
---

# Conventions

## Document types

Every Markdown file in this repo starts with YAML frontmatter, and its **first field is `type`** (the OKF convention from [HAL_md](https://github.com/thephm/hal_md)). We define the types, always with a capital first letter. The build fails if a file is missing `type` or uses one that isn't listed.

| Type | Used for |
|---|---|
| `Readme` | A folder's `README.md` |
| `Instructions` | Instructions for AI agents, like `CLAUDE.md` |
| `Brainstorm` | Idea lists |
| `Course` | A course or course edition |
| `Presentation` | A slide deck ([Marp](../references/tools/marp.md)) |
| `Slide` | One slide. Decks are built from these: see [Extending Markdown 101](../course/markdown-101/extending.md) |
| `Guide` | How-to instructions |
| `List` | A generated list of references |
| `Inbox` | Items waiting for triage |
| `Context` | Background on an environment, like [microsoft-atlassian/](../microsoft-atlassian/) |
| `Exercise` | A course exercise: starter file or answer key |
| `Cheatsheet` | A one-page handout |
| `Reference` | A lookup page, like [what works where](../microsoft-atlassian/markdown-support.md) |

Reference entries and templates use their own types (`Resource`, `App`, `Person`, and so on): see [references/README.md](../references/README.md). To add a new type, add it here and to `DOC_TYPES` in [`scripts/build_references.py`](../scripts/build_references.py).

## Reference IDs

Every reference is its own Markdown file with YAML frontmatter. Its `slug` is the permanent unique ID, and `<section>/<slug>` is its deep link, e.g. [`tools/pandoc`](../references/tools/pandoc.md). Never rename or reuse a slug. See [references/README.md](../references/README.md) for the full schema.

## Folders

| Folder | What's in it |
|---|---|
| [course/](../course/) | The Markdown 101 course, its editions, slides, and handouts |
| [references/](../references/) | One file per reference entry, plus the generated lists |
| [templates/](../templates/) | Entry templates, based on [HAL_md](https://github.com/thephm/hal_md) |
| [microsoft-atlassian/](../microsoft-atlassian/) | Markdown in a Microsoft 365, GitHub, and Confluence workplace. The core course stays tool-neutral |
| [design/](../design/) | The Marp theme for slides and handouts |
| [media/](../media/) | Source images and diagrams |
| [scripts/](../scripts/) | Build scripts for the reference lists, decks, and diagrams |
| [docs/](./) | How this repo works |

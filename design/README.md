---
type: Readme
---

# Design

One look for everything we share: slides and one-page handouts. Purple and amber, with Segoe UI on Windows (Inter elsewhere) and Cascadia Code for code.

| File | What |
|:---|:---|
| [markdown101.css](markdown101.css) | The [Marp](../references/tools/marp.md) theme `markdown101` |

## Use it

Start a Markdown file with the block below. For a slide deck, put the same settings under `frontmatter:` in its deck file instead (see [Extending Markdown 101](../course/markdown-101/extending.md)).

```yaml
---
type: Presentation    # or Cheatsheet
marp: true
theme: markdown101
footer: "Markdown 101 · [github.com/thephm/markdown](https://github.com/thephm/markdown)"
---
```

| For | Add | Size |
|:---|:---|:---|
| Slides | `paginate: true` | 16:9 |
| A one-page handout | `size: a4-portrait` and `class: cheatsheet` | A4 portrait, two columns |

Slide classes: `<!-- _class: lead -->` for title and closing slides, `<!-- _class: break -->` for section dividers.

## Preview and export

- **VS Code:** install Marp for VS Code. The repo's [`.vscode/settings.json`](../.vscode/settings.json) registers the theme, so the preview uses it. Export from the Marp button.
- **Command line:** `npm install`, then `npm run build`. HTML, PDF, and PowerPoint files land in `dist/`, which isn't committed.
- **Releases:** GitHub builds everything on each push and publishes a release for each version tag. See [Releases](../docs/building.md#releases).

Always credit the source: the `footer` links back to this repo.

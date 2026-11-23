---
type: Guide
---

# Building and releasing

## Build locally

```bash
npm install
```

```bash
npm run build
```

The slides and handouts land in `dist/` as PDF, HTML, and PowerPoint. Don't commit them.

To build only part of it, use `npm run slides` or `npm run handouts`.

## Update a diagram

Edit the `.mmd` file in [media/](../media/), then run:

```bash
npm run media
```

Commit the `.mmd` and the `.svg` together.

## Update the reference lists

After adding or changing anything in [references/](../references/), regenerate the lists and check them:

```bash
python scripts/build_references.py
```

```bash
python scripts/build_references.py --check
```

Commit the generated files. The check also fails if any Markdown file is missing its `type` (see [Conventions](conventions.md)).

## Releases

The [Course workflow](../.github/workflows/course.yml) builds the course into PDF, HTML, and PowerPoint. Generated files are never committed.

| When | What you get | Footer says |
|---|---|---|
| Every push to `main` | The `markdown-101` artifact on the workflow run | `Markdown 101 · dev-<commit>` |
| A version tag, like `v0.1` | A [GitHub Release](https://github.com/thephm/markdown/releases) with all files attached | `Markdown 101 · v0.1` |

To release a version:

```bash
git tag v0.1
```

```bash
git push origin v0.1
```

Versions have two parts, `v<major>.<minor>`. Bump the major number for a restructured course and the minor number for everything else, like new slides, sections, or fixes. Stay on `v0.x` until the course is ready to call 1.0.

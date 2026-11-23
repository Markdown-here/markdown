---
type: Readme
---

# Media

Source images for slides and handouts: photos, screenshots, and diagram exports. Commit them here and link to them with a relative path, for example `![Team photo](../../media/team.png)`.

- Use descriptive, lowercase, hyphenated names: `teams-markdown-shortcuts.png`.
- Prefer SVG for diagrams and PNG for screenshots. Keep files small.
- No real names, faces, or internal details without permission.

## Diagrams

Write diagrams in [Mermaid](../references/tools/mermaid.md) as `<name>.mmd`, then render them:

```bash
npm run media
```

That turns each changed `.mmd` into a `.svg` in the course colors from [mermaid.json](mermaid.json). Commit both files: the `.mmd` is the source, the `.svg` is what slides and GitHub show. `python scripts/render_media.py --all` re-renders everything.

The renderer drives a browser. On a work laptop, point it at Edge instead of letting it download Chrome:

```bat
set PUPPETEER_SKIP_DOWNLOAD=true
npm install
set CHROME_PATH=C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
npm run media
```

Generated files (PDF, HTML, PowerPoint) don't go here. The [Course workflow](../.github/workflows/course.yml) builds them; see [Releases](../README.md#releases).

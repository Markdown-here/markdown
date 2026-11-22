---
type: Instructions
---

# CLAUDE.md

## Git

- **Work directly on `main`.** Don't create or push other branches, including session branches like `claude/...`, unless I ask for one.
- **Ask before every push.** Commit locally, show me what would be pushed, and wait for a yes. Approval for one push doesn't cover the next one.
- Don't open pull requests unless I ask.

## Conventions

- Every `.md` file starts with frontmatter whose first field is `type`, capitalized. Allowed types are listed in [README.md](README.md#document-types).
- After adding or changing anything in `references/`, run `python scripts/build_references.py`, then `--check`. Commit the generated files.
- Slugs are permanent. Never rename or reuse one.
- Work-specific content goes in `work/`. Keep the core course tool-neutral.
- Mark anything untested at work with **(verify)**.
- Anything meant to be shared (slides, handouts) uses the `markdown101` theme in [design/](design/) and credits the repo in its footer. Render it and look at it before calling it done.
- Never commit generated files (PDF, HTML, PowerPoint). The Course workflow builds them, and version tags publish releases. Pushing a tag is a push: ask first.
- Beginner-facing tables use plain `---` separators, no alignment colons.

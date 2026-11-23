---
type: Instructions
---

# CLAUDE.md

## Git

- **Work directly on `main`.** Don't create or push other branches, including session branches like `claude/...`, unless I ask for one.
- **Ask before every push.** Commit locally, show me what would be pushed, and wait for a yes. Approval for one push doesn't cover the next one.
- Don't open pull requests unless I ask.

## Writing style

Write like a person who knows the subject, not like an AI.

- **No em dashes (—).** Use a period, comma, colon, or parentheses instead. En dashes in ranges like `0:00–0:03` are fine.
- **Plain, specific words.** No "delve", "seamless", "leverage", "robust", "unlock", "elevate", "empower", "game-changer", "landscape" (unless it means page orientation), "journey", "in today's fast-paced world".
- **No filler.** No intros that restate the title, no "In conclusion", no "It's not just X, it's Y", no lists padded to three items.
- **Short sentences, active voice.** Say what something does and why it matters to the reader.
- **Light formatting.** Bold for the few words that matter, not every other phrase. Emoji only when they carry meaning, like a ✅ / ❌ legend.
- **No hype.** Don't claim things we haven't checked. Mark them **(verify)**.

## Conventions

- Every `.md` file starts with frontmatter whose first field is `type`, capitalized. Allowed types are listed in [README.md](README.md#document-types).
- After adding or changing anything in `references/`, run `python scripts/build_references.py`, then `--check`. Commit the generated files.
- Slugs are permanent. Never rename or reuse one.
- Work-specific content goes in `work/`. Keep the core course tool-neutral.
- Mark anything untested at work with **(verify)**.
- Anything meant to be shared (slides, handouts) uses the `markdown101` theme in [design/](design/) and credits the repo in its footer. Render it and look at it before calling it done.
- Slides are one file per slide (`type: Slide`) in `slides/` folders. Deck files (`deck.yml`, `*-deck.yml`) set the order. Edit slide files, never the built deck in `dist/`. Slide IDs (file names) are permanent. See [course/markdown-101/extending.md](course/markdown-101/extending.md).
- Diagrams: edit `media/<name>.mmd`, run `npm run media`, and commit the `.mmd` and the `.svg` together.
- Never commit generated files (PDF, HTML, PowerPoint). The Course workflow builds them, and version tags publish releases. Pushing a tag is a push: ask first.
- Beginner-facing tables use plain `---` separators, no alignment colons.

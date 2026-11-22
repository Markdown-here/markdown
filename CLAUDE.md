# CLAUDE.md

## Git

- **Work directly on `main`.** Don't create or push other branches, including session branches like `claude/...`, unless I ask for one.
- **Ask before every push.** Commit locally, show me what would be pushed, and wait for a yes. Approval for one push doesn't cover the next one.
- Don't open pull requests unless I ask.

## Conventions

- After adding or changing anything in `references/`, run `python scripts/build_references.py`, then `--check`. Commit the generated files.
- Slugs are permanent. Never rename or reuse one.
- Work-specific content goes in `work/`. Keep the core course tool-neutral.
- Mark anything untested at work with **(verify)**.

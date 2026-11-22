---
type: Technology
slug: yaml
title: YAML
url: https://yaml.org/
people:
  - 
organizations:
  - 
state: active
source: "c:\notes"
added: 2026-11-22
updated: 
tags:
  - spec
  - yaml
---

# YAML

## Summary

"YAML Ain't Markup Language": a human-friendly data format used for config files and for frontmatter at the top of Markdown files.

## References

1. <https://yaml.org/>

## Notes

- Indentation with spaces shows nesting. Tabs are not allowed.
- Strings can be unquoted, single-quoted (no escapes), or double-quoted (escapes like `\n` work).
- `>` folds a block into one line; `|` keeps line breaks.
- `~` or `null` means no value.
- Most JSON converts to YAML and back.
- Python: PyYAML loads a YAML file into a dictionary (use `yaml.safe_load`).

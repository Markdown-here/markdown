---
type: Cheatsheet
---

# Markdown cheat sheet

Plain text with a few symbols. Save as `.md`.

## The core: works almost everywhere

| You want | You type |
|---|---|
| Heading | `# Title`, `## Section`, `### Subsection` |
| Paragraph | Leave a **blank line** between paragraphs |
| Bold | `**bold**` |
| Italic | `*italic*` or `_italic_` |
| Bulleted list | `- item` (indent two spaces to nest) |
| Numbered list | `1. item` |
| Link | `[text](https://example.com)` |
| Image | `![description](picture.png)` |
| Inline code | `` `code` `` |
| Code block | Three backticks, then the language: ` ```python ` … ` ``` ` |
| Quote | `> quoted text` |
| Divider | `***` or `---` on its own line |

## Level up: GitHub Flavored Markdown

| You want | You type |
|---|---|
| Table | `\| Name \| Due \|`, then `\|---\|---\|`, then one row per line |
| Task list | `- [ ] to do` and `- [x] done` |
| Strikethrough | `~~old~~` |
| Diagram | A code block with the language `mermaid` |

Works on GitHub and in most editors, but not always in chat apps.

## Gotchas

- **No blank line, no new paragraph.** Two lines in a row join into one.
- **Put a space after the symbol:** `# Title`, not `#Title`.
- **Show a symbol as-is** with a backslash: `\*not italic\*`.
- **Chat apps have their own rules.** The same characters can mean something else there.

## Learn more

- [Markdown Guide](https://www.markdownguide.org/)
- [CommonMark: learn Markdown in 60 seconds](https://commonmark.org/help/)
- [GitHub's basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

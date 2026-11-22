---
type: Cheatsheet
marp: true
footer: "Markdown 101 · [github.com/thephm/markdown](https://github.com/thephm/markdown)"
theme: markdown101
size: a4
class: cheatsheet
---

# Markdown cheat sheet: Microsoft edition

Plain text with a few symbols. Save as `.md`. Our standard is GitHub Flavored Markdown.

## Where to write it

- **VS Code:** preview with `Ctrl+Shift+V`, side by side with `Ctrl+K V`
- **OneDrive:** *Add New* › *Markdown Document*
- **Notepad** on Windows 11 **(verify)**
- **Copilot:** ask it to "answer in Markdown" or "turn this into Markdown"

## The core: works everywhere

| You want | You type |
|---|---|
| Heading | `# Title` and `## Section` |
| Paragraph | A **blank line** between |
| Bold | `**bold**` |
| Italic | `*italic*` or `_italic_` |
| Bullets | `- item` |
| Numbers | `1. item` |
| Link | `[text](url)` |
| Image | `![alt text](pic.png)` |
| Code | `` `code` `` |
| Code block | ` ```python ` … ` ``` ` |
| Quote | `> text` |
| Divider | `***` on its own line |

## Level up: in files, not chat

| You want | You type |
|---|---|
| Task list | `- [ ] to do`, `- [x] done` |
| Table | `\| A \| B \|` then `\|---\|---\|` |
| Strikethrough | `~~old~~` |
| Diagram | ` ```mermaid ` code block |

## Teams is not Markdown

| You type | In Markdown | In Teams chat |
|---|---|---|
| `*text*` | *italic* | **bold** |
| `_text_` | *italic* | *italic* |
| `` `text` `` | `code` | `code` |
| A table | a table | plain text |

In chat, stick to bold, italic, and code. **(verify)** every row in Teams.

## Gotchas

- **No blank line, no new paragraph.** Two lines in a row join into one.
- **Nest a list** by indenting two spaces.
- **Put a space after the symbol:** `# Title`, not `#Title`.
- **Show a symbol as-is** with a backslash: `\*not italic\*`.

## VS Code extensions

- **markdownlint** checks your style
- **Marp for VS Code** makes slides from Markdown
- A **Mermaid preview** extension draws diagrams **(verify names)**

## Learn more

- [Markdown Guide](https://www.markdownguide.org/)
- [CommonMark: learn Markdown in 60 seconds](https://commonmark.org/help/)
- [Use Markdown formatting in Teams](https://support.microsoft.com/en-us/office/use-markdown-formatting-in-teams-4d10bd65-55e2-4b2d-a1f3-2bebdcd2c772)

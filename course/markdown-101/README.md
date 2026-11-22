---
type: Course
---

# Markdown 101 — 30 minutes

**Goal:** Everyone leaves able to write a clean README, meeting notes, or chat message in Markdown, and knows where to learn more.

**Format:** Live, hands-on. Attendees type along in any editor with a preview, such as [VS Code](../../references/tools/vs-code.md) (`Ctrl+Shift+V`) or [Obsidian](../../references/tools/obsidian.md), or in a chat or GitHub comment box.

## Editions

The core course below is tool-neutral. An edition keeps the same structure and timing but swaps in the tools and examples the audience already uses.

| Edition | For | What changes |
|:---|:---|:---|
| Core (this page) | Anyone | Nothing, uses general examples |
| [Microsoft](editions/microsoft.md) | Workplaces on Microsoft 365 | VS Code, Notepad, OneDrive, Teams, Copilot; leads into docs-as-code with GitHub and Confluence |

## Agenda

| Time | Segment | Key points |
|:---|:---|:---|
| 0:00–0:03 | **Hook** | Same text shown raw vs rendered. "You already use Markdown": chat apps, GitHub READMEs, AI chatbot answers |
| 0:03–0:06 | **What and why** | 2004, Gruber + Swartz. Plain text, readable raw, portable, future-proof, diffable, AI-native |
| 0:06–0:16 | **The core 80%** (live) | Headings, paragraphs, **bold**/*italic*, lists (bulleted, numbered, nested), links, images, `inline code`, fenced code blocks, blockquotes, horizontal rules |
| 0:16–0:21 | **Level up** | Task lists `- [ ]`, tables, Mermaid diagram teaser. Flavors: CommonMark vs GFM vs chat-app formatting |
| 0:21–0:26 | **Exercise** | Rewrite a messy plain-text meeting note into well-structured Markdown (starter file provided) |
| 0:26–0:27 | **Wrap** | Cheat sheet handout, top tools and resources, where to go next |
| 0:27–0:29 | **Q&A** | Questions come before the close, so the audience doesn't get the last word |
| 0:29–0:30 | **Close** | One line: "You type `*this*`, you get *this*. That's Markdown!" Then stop |

## Materials to build

Shared by all editions unless an edition says otherwise.

- [ ] Slides (written in Markdown, naturally, with [Marp](../../references/tools/marp.md); see [Slide tool](#slide-tool)). Done for the [Microsoft edition](editions/microsoft-slides.md); a core deck can be cut from it
- [x] [`cheatsheet.md`](cheatsheet.md): one page, printable
- [x] [`exercise-before.md`](exercise-before.md) / [`exercise-after.md`](exercise-after.md): the meeting-notes rewrite
- [ ] Demo script with exact keystrokes so the live part stays on time
- [ ] "Next steps" page linking to [references](../../references/) by ID

## Slide tool

**Decision: [Marp](../../references/tools/marp.md).** The deck is one plain Markdown file, edited and previewed in VS Code with the Marp extension and exported to PDF and PowerPoint.

| Tool | Source | Editor | Export | Verdict |
|:---|:---|:---|:---|:---|
| [Marp](../../references/tools/marp.md) | Plain Markdown, `---` between slides | VS Code extension, live preview | HTML, PDF, PPTX (images by default) | **Chosen.** Simplest, and the source reads fine on GitHub and in OneDrive |
| [Quarto](../../references/tools/quarto.md) | Markdown plus Quarto syntax | VS Code extension | reveal.js, editable PPTX, PDF | Runner-up. Use it if an editable PowerPoint becomes a must |
| [Slidev](../../references/tools/slidev.md) | Markdown plus Vue | Any, runs a dev server | Web, PDF, PPTX, PNG | Too heavy: a Node project per deck |
| [reveal.js](../../references/tools/reveal-js.md) | HTML with Markdown inside | Any | Web; PDF via print or DeckTape | Most control, but not plain Markdown |
| [remark](../../references/tools/remark.md) | Markdown inside one HTML file | Any | Web | Simple, but barely maintained |

Comparisons: [Slidev vs Marp vs reveal.js](../../references/resources/slidev-vs-marp-vs-revealjs.md), [Marp vs reveal.js with the same content](../../references/resources/marp-vs-revealjs-classmethod.md).

The reveal at the end works with Marp too: open the `.md` file and show that the whole deck is just Markdown.

How to view, export, and present a Marp deck: [Marp: how to use it](../../references/tools/marp.md#how-to-use-it). Each edition adds its own setup, for example [presenting the Microsoft edition](editions/microsoft.md#presenting).

## Credibility boosters

- Build the deck *in Markdown* and reveal that at the end, after Q&A, as the last thing people hear
- Show an AI answer's raw Markdown: "this is why your chatbot output looks nice"
- Hand out a cheat sheet that is itself a Markdown file in a repo

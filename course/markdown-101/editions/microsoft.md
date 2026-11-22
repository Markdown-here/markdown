---
type: Course
---

# Markdown 101 — Microsoft edition

Same structure and timing as the [core course](../README.md), tuned for a workplace on Microsoft 365, GitHub, and Confluence. Background on the environment and the bigger docs-as-code goal: [work context](../../../work/README.md).

> Items marked **(verify)** need a quick test in the real environment before the session.

## Tools attendees use

| Tool | Role in the session |
|:---|:---|
| **VS Code** | Main demo editor. Split view: source left, preview right (`Ctrl+K V`) |
| **Notepad** (Windows 11) | "Nothing to install" option, with basic Markdown formatting **(verify)** |
| **OneDrive** | *Add New* › *Markdown Document* creates an `.md` file (confirmed in the iPhone app), so anyone can follow along from a phone or browser |
| **Teams chat** | The hook and the flavors example |
| **Copilot** | Proof that Markdown is everywhere: its answers are Markdown |
| **GitHub** | Where Markdown renders fully, including Mermaid |
| **Confluence** | Where most people read docs today; the closing teaser |

## Agenda

| Time | Segment | Microsoft-specific content |
|:---|:---|:---|
| 0:00–0:03 | **Hook** | Show a Teams message with `code`, then a Copilot answer, then the raw Markdown behind it. "You already use this" |
| 0:03–0:06 | **What and why** | Core content, plus: Copilot reads and writes Markdown, so docs in Markdown are docs Copilot can use |
| 0:06–0:16 | **The core 80%** (live) | Typed in VS Code with preview open. Attendees follow in VS Code, Notepad, or OneDrive |
| 0:16–0:21 | **Level up** | Task lists, tables, and a Mermaid diagram rendered in VS Code or GitHub: "this could replace your draw.io diagram". Flavors: in Teams `*bold*` is **bold**; in Markdown it's *italic* |
| 0:21–0:26 | **Exercise** | Turn a messy Teams-meeting recap into Markdown. Bonus: ask Copilot to do it, then review what it wrote |
| 0:26–0:27 | **Wrap** | Link to this course on GitHub, cheat sheet in the repo, VS Code extensions to install |
| 0:27–0:29 | **Q&A** | Before the close, never after it |
| 0:29–0:30 | **Close** | Reveal the deck is one Markdown file |

## Prep checklist

- [ ] Test every Teams formatting shortcut: `*x*`, `**x**`, `_x_`, `~x~`, `` `x` ``, lists, quotes **(verify)**
- [ ] Confirm the Notepad version on work laptops supports Markdown formatting **(verify)**
- [x] OneDrive iPhone app has *Add New* › *Markdown Document*
- [ ] Check the same option exists in OneDrive on the web and on work accounts, and that the preview renders Markdown **(verify)**
- [ ] Pick a Copilot prompt for the hook and the exercise, and test it on the day (answers vary)
- [ ] Have a draw.io diagram from a real Confluence page, redrawn in Mermaid, for the level-up
- [ ] Confirm the [Marp for VS Code](../../../references/tools/marp.md) extension (`marp-team.marp-vscode`) is allowed on work laptops, and that PDF and PPTX export work with Edge **(verify)**
- [ ] Check whether an image-only `.pptx` is acceptable when sharing in Teams. If people need to edit it, try Marp's experimental editable export or [Quarto](../../../references/tools/quarto.md) **(verify)**
- [ ] Put the exercise files in a shared OneDrive or SharePoint folder

## Presenting

How to view and show the [deck](microsoft-slides.md). For Marp in general, see [Marp](../../../references/tools/marp.md#how-to-use-it).

### Set up once

1. In VS Code, open the Command Palette (`Ctrl+Shift+P`), choose **Git: Clone**, and paste `https://github.com/thephm/markdown`.
2. Trust the folder when VS Code asks. Our purple theme only loads in a trusted folder.
3. Install **Marp for VS Code** (`Ctrl+Shift+X`).
4. Open `course/markdown-101/editions/microsoft-slides.md` and press `Ctrl+K V` to preview.

### Present

- Export to **HTML** (Marp button › **Export slide deck…**) and open it in **Edge**. Use presenter view: notes and the next slide on the laptop, slides on the big screen.
- Backup: export to **PowerPoint**. The notes come along; the slide text can't be edited.
- If the Marp extension isn't allowed, open a pre-exported HTML file in Edge.

### On the day

- Presenter notes are the `<!-- ... -->` comments in the deck: timings and what to say.
- Live demo: switch to VS Code with the preview open.
- Mermaid slide: switch to GitHub to show the diagram drawn.
- Close: open `microsoft-slides.md` and scroll through it. The whole deck is one Markdown file.

## Edition-specific materials

- [x] [Slide deck](microsoft-slides.md) in [Marp](../../../references/tools/marp.md), with presenter notes. Open it in VS Code with the Marp extension to preview, present, or export to PDF and PowerPoint. It follows the house flavor in [Which Markdown?](../../../work/README.md#which-markdown)
- [x] [`teams-recap-before.md`](teams-recap-before.md): a realistic, messy meeting recap (no real names or projects), with the answer key [`teams-recap-after.md`](teams-recap-after.md)
- [ ] Mermaid version of a familiar draw.io diagram
- [x] [Cheat sheet variant](microsoft-cheatsheet.md) with a "Teams vs Markdown" box
- [ ] Recommended VS Code extensions list: Markdown preview with Mermaid support, markdownlint **(verify names)**

## Follow-ups that build street cred

- Office hours: "bring a Confluence page, leave with a Markdown version"
- A pilot team for docs-as-code, publishing from GitHub to Confluence
- Markdown 201: diagrams-as-code with Mermaid

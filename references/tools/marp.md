---
type: App
slug: marp
title: Marp
aliases:
  - Markdown Presentation Ecosystem
  - Marp for VS Code
  - Marp CLI
url: https://marp.app/
organizations:
  - 
people:
  - 
integrations:
  - vs-code
state: active
source: https://www.pkgpulse.com/guides/slidev-vs-marp-vs-revealjs-code-first-presentations-2026
added: 2026-11-22
updated: 
tags:
  - tool
  - slides
  - editor
  - converter
  - windows
  - macos
  - linux
  - cli
  - free
  - open-source
---

# Marp

## Summary

Write a slide deck as one ordinary Markdown file. Add `marp: true` to the frontmatter and separate slides with `---`. The official **Marp for VS Code** extension shows a live slide preview next to the source and exports to HTML, PDF, and PowerPoint (`.pptx`). **Marp CLI** does the same from the command line or a GitHub Action.

The chosen slide tool for [Markdown 101](../../course/markdown-101/), because:

- The source stays plain Markdown. It reads fine on GitHub, in OneDrive, or in Notepad, even without Marp.
- It works inside VS Code with no project, Node install, or build step.
- PowerPoint and PDF export fit a Microsoft 365 workplace: share the `.pptx` in Teams, or the PDF anywhere.
- It's the simplest of the code-first slide tools to learn, which suits a course *about* simple Markdown.

## Gotchas

- Export needs a local Chrome, Edge, or Firefox. Edge is already on Windows.
- By default each `.pptx` slide is an image, so people can present it but not edit it in PowerPoint. An experimental editable PPTX export exists and needs LibreOffice **(verify)**.
- Export is turned off in VS Code's untrusted workspaces and in VS Code for the Web.
- Less interactive than [Slidev](slidev.md) or [reveal.js](reveal-js.md): no live code or click-through animations.

## References

1. <https://marp.app/>
2. <https://github.com/marp-team/marp-vscode>
3. <https://github.com/marp-team/marp-cli>

## Notes

- VS Code extension ID: `marp-team.marp-vscode`. Check that it's allowed on work laptops **(verify)**.

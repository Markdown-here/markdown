---
type: Reference
---

# Markdown at work: what works where

The same Markdown can look different in each app we use. This page compares them, with [GitHub](../references/organizations/github.md) as the baseline because it supports our house standard, GitHub Flavored Markdown (see [Which Markdown?](README.md#which-markdown)).

> Last checked: 2026-11-22. Anything marked ❓ or **(verify)** comes from documentation or reports, not from testing on our tenant yet.

## At a glance

| | Write Markdown? | Where | Flavor |
|:---|:---|:---|:---|
| **GitHub** | ✅ Files, issues, pull requests | Browser | Full GFM, plus Mermaid |
| **VS Code** | ✅ `.md` files, with live preview | Desktop | CommonMark plus GFM tables and strikethrough. More through extensions |
| **OneDrive** | ✅ `.md` files: view, edit, or split view | Browser, iPhone, Android | Native since 2026. Flavor not documented **(verify)** |
| **SharePoint** | ✅ `.md` files in libraries, and the Markdown web part on pages | Browser | Files: same editor as OneDrive. Web part: [Marked.js](https://marked.js.org/) |
| **Teams chat** | ⚠️ Typing shortcuts only | Desktop and web. Mobile can show it but not create it | Its own "Markdown-style" rules |
| **Confluence Cloud** | ⚠️ Typing shortcuts, and pasting sometimes | Browser | None. Pages are stored in Confluence's own format |

## Feature by feature

✅ works · ⚠️ works differently · ❌ doesn't work · ❓ not confirmed

| Feature | You type | GitHub | VS Code | OneDrive and SharePoint files | SharePoint web part | Teams chat | Confluence Cloud |
|:---|:---|:---|:---|:---|:---|:---|:---|
| Headings | `# Title` | ✅ | ✅ | ✅ | ✅ | ✅ Levels 1 to 3 | ⚠️ As you type ❓ |
| Bold | `**bold**` | ✅ | ✅ | ✅ | ✅ | ⚠️ Use `*bold*` | ⚠️ As you type ❓ |
| Italic | `*italic*` | ✅ | ✅ | ✅ | ✅ | ⚠️ Use `_italic_` | ⚠️ `_italic_` as you type ❓ |
| Strikethrough | `~~text~~` | ✅ | ✅ | ❓ | ✅ ❓ | ⚠️ Use `~text~` | ⚠️ As you type ❓ |
| Lists | `- item`, `1. item` | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ As you type ❓ |
| Links | `[text](url)` | ✅ | ✅ | ✅ | ✅ | ✅ | ❓ |
| Images | `![alt](file.png)` | ✅ | ✅ | ✅ | ✅ | ❌ Paste the image instead | ❌ Insert the image instead |
| Inline code | `` `code` `` | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ As you type ❓ |
| Code block | Three backticks | ✅ Highlighted | ✅ Highlighted | ✅ Highlighted | ✅ | ✅ | ⚠️ As you type ❓ |
| Blockquote | `> quote` | ✅ | ✅ | ✅ ❓ | ✅ | ✅ | ⚠️ As you type ❓ |
| Table | Pipes and dashes | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ Use the table button |
| Task list | `- [ ] task` | ✅ Tickable | ⚠️ Shows boxes, can't tick ❓ | ✅ Checkboxes | ✅ ❓ | ❌ | ⚠️ `[]` as you type makes a Confluence task ❓ |
| Mermaid diagram | ` ```mermaid ` | ✅ | ⚠️ With an extension | ❓ Not mentioned | ❌ Needs a third-party web part | ❌ | ⚠️ With a Marketplace app ❓ |
| Frontmatter | `---` block at the top | ⚠️ Shown as a table | ✅ Hidden in the preview | ❓ | ❓ | ❌ | ❌ |

## Notes per app

### VS Code

- Preview with `Ctrl+Shift+V`, or side by side with `Ctrl+K V`.
- Built on CommonMark. Extensions add more, for example Mermaid diagrams ([Markdown Preview Mermaid Support](https://github.com/mjbvz/vscode-markdown-mermaid)) and style checks ([markdownlint](../references/tools/markdownlint.md)).
- Test task lists in our VS Code version, because reports disagree on how they show. **(verify)**

### OneDrive

- Since 2026, `.md` files open in a built-in editor in the browser. It has View, Edit, and Split modes, and a formatting toolbar.
- To create one: *+ Create or upload* › *Markdown document* on the web, or *Add New* › *Markdown Document* in the iPhone app (tested).
- Reports say tables, checkboxes, links, and highlighted code blocks render. Nothing says Mermaid or frontmatter do. **(verify)**
- Your organization's admins may be able to block it. **(verify)** that it's turned on for us.

### SharePoint

- **`.md` files** in a document library use the same editor as OneDrive.
- **Markdown web part** shows Markdown on a SharePoint page. It uses Marked.js, and its properties pane links to a syntax reference. It isn't available in SharePoint Server 2019.
- Mermaid on a page needs a third-party web part.

### Teams chat

- Teams calls it Markdown, but Microsoft says it "doesn't fully match standard Markdown".
- The big trap is `*text*`, which means **bold** in Teams but *italic* in Markdown.
- No tables, task lists, or images in chat.
- On mobile you can read formatted messages but not write them.

### Confluence Cloud

- No Markdown mode. Some Markdown turns into formatting as you type. Pasted Markdown converts only some of the time, depending on the browser and the editor.
- Pages are stored in Confluence's own format, so Markdown isn't kept.
- That's why we write in Git and publish to Confluence: see the [docs-as-code pipeline](README.md#docs-as-code-pipeline-spec-sketch).

## What this means for us

1. **Write files in GitHub Flavored Markdown.** It works in GitHub, VS Code, OneDrive, and SharePoint.
2. **In Teams, stick to the basics:** `_italic_`, `` `code` ``, code blocks, lists, and links. Watch out for `*`.
3. **Don't write in Confluence. Publish to it.**
4. **For diagrams, use Mermaid on GitHub and in VS Code.** Export an image for places that can't draw it.

## Sources

- [Use Markdown formatting in Microsoft Teams](https://support.microsoft.com/en-US/teams/chat/use-markdown-formatting-in-microsoft-teams) (Microsoft Support)
- [Use the Markdown web part](https://support.microsoft.com/en-us/sharepoint/sites-pages/use-the-markdown-web-part) (Microsoft Support)
- [Introducing Markdown support in SharePoint and OneDrive](https://techcommunity.microsoft.com/blog/onedriveblog/introducing-markdown-support-in-sharepoint-and-onedrive/4512174) (Microsoft OneDrive blog, 2026)
- [Native Markdown editing now in OneDrive and SharePoint](https://office-watch.com/2026/markdown-editing-onedrive-sharepoint/) (Office Watch, 2026)
- [MC1423113: Create, view, and edit Markdown files in OneDrive mobile](https://mc.merill.net/message/MC1423113) (Message Center)
- [Markdown in Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown) (VS Code docs)
- [How to insert Markdown text into my Confluence page](https://community.atlassian.com/forums/Confluence-questions/How-to-insert-markdown-text-into-my-Confluence-Page/qaa-p/3037606) (Atlassian Community)

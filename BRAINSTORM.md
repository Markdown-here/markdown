# Brainstorm

> Living document. Ideas first, judgment later.

## The pitch

**One destination for anyone who wants to learn Markdown, try it, or find the best resources about it** — designed so that humans *and* AI agents get first-class experiences.

## Audiences

- **Newcomers** — "what is this and why does everyone use it?"
- **Everyday writers** — notes, docs, READMEs, chat apps
- **Power users** — flavors, extensions, diagrams, math, static sites
- **AI builders** — Markdown is the lingua franca of LLM input/output
- **Teams** — internal training (hello, Markdown 101)

## Site sections

1. **Learn** — Markdown 101 course, then 201 (tables, footnotes, task lists, Mermaid), flavor deep-dives (CommonMark, GFM, Obsidian, MultiMarkdown, MDX)
2. **Try** — live split-pane playground; flavor switcher showing how the same source renders differently; "fix this broken Markdown" challenges
3. **Reference / Cheat sheet** — every syntax element, one page each, with examples, gotchas, and per-flavor support matrix
4. **Resources** — curated articles, specs, guides, videos, books
5. **Tools** — editors, converters, linters, renderers, tagged by platform (`#ios #android #windows #macos #linux #web #cli`) and by kind (`#editor #converter #linter #notes #static-site`)
6. **People** — the creators, maintainers, and educators (HAL_md People template)
7. **Organizations** — spec bodies, companies, projects (HAL_md Organization template)
8. **Markdown + AI** — prompting with Markdown, why LLMs output it, `llms.txt`, Markdown for RAG/chunking, agent instruction files (`CLAUDE.md`, `AGENTS.md`)
9. **History / Timeline** — 2004 Gruber + Swartz → CommonMark → GFM → today
10. **Gallery** — beautiful real-world Markdown (READMEs, docs sites, notes vaults)

## AI-first ideas

- Every page has **"Copy as Markdown"** and a raw `.md` URL
- Publish **`/llms.txt`** and **`/llms-full.txt`** (see [llmstxt.org](https://llmstxt.org/))
- References exported as **JSON / JSON-LD** alongside the Markdown, generated from the same source
- Stable IDs mean an agent can cite `tool-0003` and a human can click it
- An **MCP server** that exposes search over references and the cheat sheet
- "Ask about this page" box powered by an LLM grounded on site content
- Prompt library: "convert this to Markdown", "lint my Markdown", etc.

## Gorgeous ideas

- Live-rendering hero: type Markdown, watch the page style itself
- Side-by-side source/render on every example, toggle per flavor
- Dark mode, great typography, keyboard-first navigation
- Tag-filterable tool directory with platform icons

## Reference data principles

- **Markdown is the source of truth** — everything else is generated
- **Every entry has:** unique ID, deep link, state, source, and is well formed (lintable)
- **IDs are permanent** — never renumbered, never reused; retired entries keep their ID with state `retired`
- Validate with a script in CI (required fields, unique IDs, valid states, link checks)

## Roadmap (rough)

1. **Now:** Markdown 101 course + seed the references lists
2. Pull in existing notes from `c:\notes`
3. Validator script + CI (markdownlint + ID/field checks)
4. Pick a site generator (Astro / VitePress / Docusaurus — decide later) and ship v0
5. Playground, cheat sheet, flavor matrix
6. AI layer: llms.txt, JSON export, MCP server

## Open questions

- [ ] Share the HAL_md People and Organization templates so the entries here match
- [ ] One big file per section, or one file per entry (with generated index)? Starting with one file per section; switch once there are ~100+ entries
- [ ] Site name / domain
- [ ] Contributions from others? (PR template, contribution guide)

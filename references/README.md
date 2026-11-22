# References

Curated, well-formed, AI-friendly references. **One Markdown file per entry**, using [HAL_md](https://github.com/thephm/hal_md)-style templates, so entries can move between this site and an Obsidian vault.

| Section | Folder | Template | Generated list |
|:---|:---|:---|:---|
| Resources | [`resources/`](resources/) | [Resource.md](../templates/Resource.md) | [resources.md](resources.md) |
| Tools | [`tools/`](tools/) | [Tool.md](../templates/Tool.md) | [tools.md](tools.md) |
| People | [`people/`](people/) | [Person.md](../templates/Person.md) | [people.md](people.md) |
| Organizations | [`organizations/`](organizations/) | [Organization.md](../templates/Organization.md) | [organizations.md](organizations.md) |

Everything is also exported to [`references.json`](references.json) for AI agents and the site.

## Unique ID and deep link

- The **`slug`** is the unique ID: lowercase, hyphenated, and the same as the filename (`pandoc` → `tools/pandoc.md`).
- The **ID** is `<section>/<slug>`, e.g. `tools/pandoc`. That's the deep link in the repo, and it'll be the site URL (`/tools/pandoc`).
- **Slugs are permanent.** Never rename or reuse one. To retire an entry, set `state: retired` and keep the file.
- Cross-references use slugs: `people: [john-macfarlane]`, `organizations: [commonmark]`. The build fails if a slug doesn't exist.

## Common fields

| Field | Required | Notes |
|:---|:---|:---|
| `type` | yes | `Resource`, `App` (tools), `Person`, or `Organization`. First property, per HAL_md's OKF convention |
| `slug` | yes | Unique ID, matches the filename |
| `title` | yes* | Display name (*people use `first_name` + `last_name`) |
| `url` | yes | Canonical link |
| `state` | yes | See states below |
| `source` | yes | Where it came from: `personal use`, `c:\notes`, a slug like `people/john-gruber`, or a URL |
| `added` | yes | `YYYY-MM-DD` |
| `updated` | no | `YYYY-MM-DD` of the last meaningful change |
| `tags` | no | List, without `#`. Obsidian shows them as `#tags` |

Each template also keeps its HAL_md-specific fields (`organizations`, `people`, `integrations`, `skills`, and so on) and body sections (`## Summary`, `## Bio`, `## References`, `## Positions`, and so on).

## States

| State | Meaning |
|:---|:---|
| `draft` | Captured, not yet reviewed |
| `active` | Reviewed and recommended |
| `watch` | Interesting, keeping an eye on it |
| `stale` | Unmaintained or outdated, kept for context |
| `broken` | Link is dead, needs attention |
| `retired` | No longer recommended, hidden from lists; slug kept forever |

## Tag vocabulary

- **Platform:** `windows` `macos` `linux` `ios` `android` `web` `cli`
- **Kind (tools):** `tool` (always) `editor` `notes` `converter` `linter` `renderer` `static-site` `diagram` `library`
- **Resource type:** `spec` `guide` `tutorial` `cheatsheet` `video` `book` `article` `ai`
- **Cost:** `free` `paid` `freemium` `open-source`

## Adding an entry

1. Copy the template from [`templates/`](../templates/) into the right folder as `<slug>.md`.
2. Fill in the frontmatter and body.
3. Run the build script, which checks every entry and regenerates the lists and JSON:

   ```bash
   python scripts/build_references.py
   ```

A GitHub Action runs `--check` on every push, so broken entries and out-of-date lists fail the build.

## Books

Books are Resources with the `book` tag, using [Book.md](../templates/Book.md):

- `people` lists the authors' slugs, `organizations` the publisher's.
- `read` is the date you finished it (`YYYY-MM-DD`), `rating` is 1–5, `format` is `ebook`, `print`, or `audio`.
- Your notes go in the body: **Summary**, **Key takeaways**, **Quotes**, **Notes**.

## Editing in Obsidian

This repo works as an Obsidian vault, or as a folder inside your vault.

- **Settings → Files and links:** turn off **Use [[Wikilinks]]**, and set **New link format** to **Relative path to file**. Links then work on GitHub and on the site too.
- **Settings → Templates:** point the template folder at `templates/`.
- Run the build script before committing, or let the GitHub Action tell you what to fix.

## Style

- Left-align table columns (`|:---|`). Center a column only when its content is centered.

# References

Curated, well-formed, AI-friendly reference lists.

| List | ID prefix | File |
|---|---|---|
| Resources | `res-` | [resources.md](resources.md) |
| Tools | `tool-` | [tools.md](tools.md) |
| People | `per-` | [people.md](people.md) |
| Organizations | `org-` | [organizations.md](organizations.md) |

## Entry schema

Each entry is an H3 heading preceded by an HTML anchor, then a field list:

```markdown
<a id="tool-0001"></a>

### Obsidian

- **ID:** `tool-0001`
- **URL:** <https://obsidian.md>
- **State:** active
- **Source:** personal use
- **Added:** 2026-11-22
- **Tags:** #editor #notes #windows #macos #linux #ios #android

One or two sentences on what it is and why it's worth knowing.
```

### Fields

| Field | Required | Notes |
|---|---|---|
| ID | yes | `<prefix>-<4 digits>`, lowercase, permanent, never reused |
| URL | yes | Canonical link, in `<angle brackets>` |
| State | yes | See states below |
| Source | yes | Where the reference came from (e.g. `personal use`, `c:\notes`, a person's ID, a URL) |
| Added | yes | ISO date `YYYY-MM-DD` |
| Updated | no | ISO date of last meaningful change |
| Tags | no | Space-separated `#tags` (see tag vocabulary) |

### Deep links

The `<a id="…">` anchor is the deep link and never changes, even if the title does:
`references/tools.md#tool-0001`. (Heading-slug anchors break when a title is edited; explicit IDs don't.)

### States

| State | Meaning |
|---|---|
| `draft` | Captured, not yet reviewed |
| `active` | Reviewed and recommended |
| `watch` | Interesting, keeping an eye on it |
| `stale` | Unmaintained or outdated, kept for context |
| `broken` | Link is dead, needs attention |
| `retired` | Removed from recommendations; ID is kept forever |

### Tag vocabulary

- **Platform:** `#windows` `#macos` `#linux` `#ios` `#android` `#web` `#cli`
- **Kind:** `#editor` `#notes` `#converter` `#linter` `#renderer` `#static-site` `#diagram` `#library`
- **Resource type:** `#spec` `#guide` `#tutorial` `#cheatsheet` `#video` `#book` `#article`
- **Cost:** `#free` `#paid` `#freemium` `#open-source`

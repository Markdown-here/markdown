# Templates

One template per reference type. They follow the [HAL_md templates](https://github.com/thephm/hal_md/tree/main/templates) so entries move freely between this site and a HAL_md / Obsidian vault, with a few site-specific fields added.

| Template | `type` | HAL_md origin | Folder |
|:---|:---|:---|:---|
| [Resource.md](Resource.md) | `Resource` | `resource` tag (OKF) | `references/resources/` |
| [Book.md](Book.md) | `Resource` + `book` tag | `resource` tag (OKF) | `references/resources/` |
| [Tool.md](Tool.md) | `App` + `tool` tag | [Product.md](https://github.com/thephm/hal_md/blob/main/templates/Product.md), OKF `tool=App` | `references/tools/` |
| [Person.md](Person.md) | `Person` | [Person.md](https://github.com/thephm/hal_md/blob/main/templates/Person.md) | `references/people/` |
| [Organization.md](Organization.md) | `Organization` | [Organization.md](https://github.com/thephm/hal_md/blob/main/templates/Organization.md) | `references/organizations/` |

## Differences from HAL_md

- **`type`** is the first property, following `okf_convert`, instead of a `person` / `organization` tag.
- **Added for the site:** `title`, `state`, `source`, `added`, `updated`.
- **Dropped from Person:** private contact fields (`mobile`, `phone`), `Life Events`, and `Communications`. These are public reference pages.
- **Links:** relative Markdown links like `[Pandoc](../tools/pandoc.md)` instead of `[[wikilinks]]`, so they work on GitHub, on the site, and in Obsidian.

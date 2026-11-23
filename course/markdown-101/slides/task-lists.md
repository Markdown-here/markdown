---
type: Slide
---

## Task lists

**You type:**

```markdown
- [x] Book the room
- [ ] Send the agenda
- [ ] Order coffee
```

**You get:**

<style scoped>
ul:last-of-type { list-style: none; padding-left: 0.2em; }
ul:last-of-type li::marker { content: ""; }
</style>

- ☑ Book the room
- ☐ Send the agenda
- ☐ Order coffee

<!--
The slide fakes the checkboxes with ☑ and ☐, because the slide tool doesn't draw task lists. GitHub shows real checkboxes you can tick: show it there.
-->

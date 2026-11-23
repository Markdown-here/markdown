---
type: Slide
---

## Diagrams as code

![bg right:30% 58%](../../../../media/confluence-publishing-flow.svg)

````markdown
```mermaid
flowchart TB
    org_dept_BusinessAnalyst[Write in VS Code]
    org_dept_Manager[Review on GitHub]
    org_dept_ProjectTeamMember[Read in Confluence]
    org_dept_BusinessAnalyst -->|Commit and push| org_dept_Manager
    org_dept_Manager -->|GitHub Action publishes| org_dept_ProjectTeamMember
```
````

- GitHub draws this as a diagram
- Change a word, the diagram updates
- `TB` is Top-to-Bottom, `LR` is Left-to-Right
- This will replace draw.io diagrams

<!--
The picture on the right is media/confluence-publishing-flow.svg, exported from media/confluence-publishing-flow.mmd. Marp doesn't draw Mermaid itself, which is a nice reminder that flavors differ. Switch to GitHub or VS Code (with a Mermaid extension) to show it drawing live.
The GitHub Action that publishes to Confluence is the workflow this diagram describes (verify it's set up before you promise it).
-->

---
name: "Prepare Commit"
description: "Inspect current changes, enforce docs gate rules, and create a compliant commit when ready."
agent: "Commit Coach"
argument-hint: "Optional: context for commit scope and message"
---
Prepare a commit for current repository changes.

Follow commit and docs-gate rules from `AGENTS.md`. Use provided context to refine scope, title, and body.

If commit succeeds and all changes are committed, the response must end with a `### Next Step` section containing exactly this command block:

```text
/Open PR
```

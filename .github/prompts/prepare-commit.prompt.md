---
name: "Prepare Commit"
description: "Inspect current changes, enforce docs gate rules, and create a compliant commit when ready."
agent: "Commit Coach"
argument-hint: "Optional: context for commit scope and message"
---
Prepare a commit for current repository changes.

Follow commit and docs-gate rules from `AGENTS.md`. Use provided context to refine scope, title, and body.

When commit succeeds and all changes are committed, finish with `/Open PR` in a command block.

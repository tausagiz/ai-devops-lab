---
name: "Prepare Commit"
description: "Inspect current changes, enforce docs gate rules, and create a compliant commit when ready."
agent: "Commit Coach"
argument-hint: "Optional: context for commit scope and message"
---
Prepare a commit for current repository changes.

Apply repository commit rules and docs gate. If changes are coherent, auto-fix docs gate by staging already-modified docs files when possible, then create commit. If blocked, report exact reason. Use provided context to refine scope/title/body.

When commit succeeds and all changes are committed, finish with `/Open PR` in a command block.

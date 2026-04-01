---
name: "Prepare Commit"
description: "Inspect current changes, enforce docs gate rules, and create a compliant commit when ready."
agent: "Commit Coach"
argument-hint: "Optional: context for commit scope and message"
---
Prepare a commit for current repository changes.

Follow commit and docs-gate rules from `AGENTS.md`. Use provided context to refine scope, title, and body.

If commit succeeds and all changes are committed:
- include one short, friendly sentence naming the next slash command (either `/Open PR` if this closes the work, or `/New Branch` if more work is planned),
- then end with a `### Next Step` section containing that command block.

If the right next step is unclear from context, ask briefly: "Is this the final commit for this branch, or do you have more changes planned?"

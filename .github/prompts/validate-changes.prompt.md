---
name: "Validate Changes"
description: "Run local checks for the current branch, report readiness, and suggest how to fix failures."
agent: "Validate Changes"
argument-hint: "Optional: validation scope (default, narrow, full)"
---
Validate this branch before commit or PR.

Use the validation scope from `AGENTS.md`: default by default, narrow only when explicitly requested with skipped checks called out, and full only when explicitly requested. Report readiness for `/Prepare Commit` or `/Open PR`.

If any check fails or required checks are skipped, include a `Suggested Fix` section with one concrete next action to unblock.

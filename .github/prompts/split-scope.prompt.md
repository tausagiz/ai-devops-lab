---
name: "Split Scope"
description: "Safely split a high-drift branch into smaller branches while preserving the original branch until deployments are verified."
agent: "Split Scope"
argument-hint: "Required: split intent (target branch themes). Optional: base branch"
---
Safely split this branch into smaller reviewable branches.

Follow `AGENTS.md` scope-drift and git safety rules. Preserve the original branch and keep a backup branch until split branches are deployed and verified.

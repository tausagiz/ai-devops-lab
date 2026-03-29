---
name: "New Branch"
description: "Start new work: describe what you plan to build and the agent will sync main and create the right branch."
agent: "Branch Coach"
argument-hint: "Required: short description of planned work (e.g. 'add restart command to CLI')"
---
Prepare a fresh feature branch for the work I am about to start.

Fetch the latest `main`, fast-forward the local branch to match origin, and create a properly named branch based on my description of the planned work.

Follow the branch naming convention from `AGENTS.md`: `type/short-slug` using only allowed type prefixes.
Choose the prefix from the kind of work I describe and prefer predictable `area-object` slugs such as `feat/cli-restart-command` or `docs/readme-agent-workflow`.

This prompt must create the new branch only from an updated `main`, never from another feature branch.

If my worktree has uncommitted changes, stop and tell me to clean it up before switching branches.

If I provided a description in the prompt arguments, use it to derive the branch name. Otherwise ask me for a brief description of the planned work.

Report:
- The update status of `main` (was it already current or fast-forwarded),
- The exact branch name that was created,
- A confirmation that the branch is active and ready for the first commit.

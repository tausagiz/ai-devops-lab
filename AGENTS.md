# AGENTS

This file summarizes guidance for AI agents ingesting this repository.

## Purpose

- DevOps learning project: automated Docker lifecycle with Python.
- Avoid rewrites of business logic; focus on build/run/log management.

## Repository structure (as of current branch)

```
src/docker_automation/
  cli.py            — CLI entry point, dispatches subcommands
  config.py         — IMAGE_TAG, BUILD_PATH constants
  docker_client.py  — get_client() factory (mockable in tests)
  commands/
    build.py        — build_image()
    run.py          — run_container()
    logs.py         — show_logs()
    clean.py        — cleanup()
tests/
  unit/             — per-command unit tests, Docker SDK mocked
  integration/      — CLI smoke tests, no daemon required
scripts/
  check_docs.py     — CI commit-message and docs-gate checker
.github/workflows/
  docs-check.yml    — commit format + docs requirement
  tests.yml         — pytest unit + integration + coverage
```

## How to use for agents

1. Read `README.md` for overall intent and usage.
2. To understand a command: read its module in `src/docker_automation/commands/`.
3. To add a command: create `src/docker_automation/commands/<name>.py` and register in `cli.py`.
4. All Docker access goes through `get_client()` from `docker_client.py` — patch that in tests.
5. Constants (image tag, build path) live in `config.py` — not scattered in functions.
6. Process `Dockerfile` for base image and default runtime behavior.

## Commit Policy

**CRITICAL**: Only the "Prepare Commit" prompt (`.github/prompts/prepare-commit.prompt.md`) is allowed to create commits automatically.

- The Commit Coach agent is invoked ONLY via the `/Prepare Commit` prompt. It never commits in response to routine file modification requests.
- All other agents, prompts, and modes **must never commit or push without explicit user request**.
- The "Prepare Commit" prompt invokes the Commit Coach agent to auto-commit only when:
  1. The user explicitly invoked the "Prepare Commit" prompt in VS Code chat.
  2. All changes are coherent (related scope).
  3. Docs gate is satisfied (README.md or AGENTS.md included if code changed).
  4. `python scripts/check_docs.py` validates the commit message format.
- **Auto-fix capability:** When docs gate violations are detected (code changes without README.md or AGENTS.md), Commit Coach automatically stages the required docs files if they have unstaged changes. Only existing unstaged changes are staged; new content is never created.
- Other agents (default mode, PR Coach, etc.) must:
  - Inspect changes without committing.
  - Ask the user before taking git actions.
  - Let Commit Coach handle commit operations when needed.

## GitHub Copilot

- Copilot can leverage this file plus repo contents.
- No duplication is needed; link agent behavior from here.
- Recommend adding `.github/copilot.yml` for custom assistant instructions (optional).
- Workspace customizations for commit preparation live in:
  - `.github/agents/commit-coach.agent.md`
  - `.github/prompts/prepare-commit.prompt.md`
- Workspace customizations for PR preparation live in:
  - `.github/agents/pr-coach.agent.md`
  - `.github/prompts/open-pr.prompt.md`
- Workspace customizations for workflow help live in:
  - `.github/agents/workflow-help.agent.md` — lists the available workflow prompts like a concise help screen.
  - `.github/prompts/workflow-help.prompt.md`
- Workspace customizations for branch lifecycle live in:
  - `.github/agents/branch-coach.agent.md` — syncs main and creates a named feature branch.
  - `.github/agents/close-branch.agent.md` — verifies merge, deletes branch, returns to updated main.
  - `.github/prompts/new-branch.prompt.md`
  - `.github/prompts/close-branch.prompt.md`
- Workspace customizations for local validation live in:
  - `.github/agents/validate-changes.agent.md` — runs local checks and reports whether the branch is ready for commit or PR.
  - `.github/prompts/validate-changes.prompt.md`
- Use the `Prepare Commit` prompt in VS Code chat to create commits. When successful, it outputs a ready-to-click `/Open PR` command at the end.
- Use the `Open PR` prompt in VS Code chat to finalize and push the PR. This prompt:
  1. Syncs the feature branch with main (asks merge or rebase preference if needed)
  2. Re-runs local validation (`pytest` and `python scripts/check_docs.py`) before push
  3. Validates all commits together at PR scope with `python scripts/check_docs.py`
  4. Pushes the branch and creates the PR
  - Supports both `merge` and `rebase` strategies for updating from main.
- Use the `Workflow Help` prompt in VS Code chat to get a concise list of the available workflow commands and when to use them.
- Use the `New Branch` prompt in VS Code chat to start new work: describe what you plan to build and the agent syncs main and creates the branch.
- Use the `Validate Changes` prompt in VS Code chat before committing or opening a PR to run the local checks expected for this repo.
- Use the `Close Branch` prompt in VS Code chat after a PR is merged to delete the feature branch and return to the latest main.

## PR-scope validation workflow (recommended)

- Instead of validating each commit independently, the full PR is validated at submission time. This allows docs updates to be scoped to the entire feature rather than individual commits.
- Script: `scripts/check_docs.py` (renamed from `check-docs.py` to follow Python snake_case).

- Current checker details in this repo:
  - Commit message format: `type(scope): summary` or `type: summary`.
  - Allowed types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `build`, `ci`.
  - Auto-generated merge commits are accepted (for example `Merge <sha> into <sha>`).
  - Docs gate requires at least one docs file in the changed set: `README.md` or `AGENTS.md`.
  - Changed set in CI is determined from GitHub event SHAs for deterministic behavior:
    - pull request: `base.sha...head.sha`
    - push: `before..after`

- Commit message template for agent-assisted writing:
  - `type(scope): concise summary` (e.g., `feat(docker): add restart workflow`)
  - body: 1) what changed, 2) why, 3) docs updated (README, AGENTS, etc.).

- CI/PR automation:
  - `docs-check.yml` — enforces commit message format + docs update requirement.
  - `tests.yml` — runs `pytest tests/unit` and `pytest tests/integration` on every PR and push to `main`.
  - Optional: use Copilot to draft commit message and docs text for maintainers to review.

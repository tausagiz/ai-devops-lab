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

## GitHub Copilot

- Copilot can leverage this file plus repo contents.
- No duplication is needed; link agent behavior from here.
- Recommend adding `.github/copilot.yml` for custom assistant instructions (optional).
- Workspace customizations for commit preparation live in:
  - `.github/agents/commit-coach.agent.md`
  - `.github/prompts/prepare-commit.prompt.md`
- Use the `Prepare Commit` prompt in VS Code chat to inspect current changes, validate docs-gate requirements, and create a compliant commit when the worktree is ready.
- After each commit the agent runs `python scripts/check_docs.py` locally — this mirrors exactly what CI checks and catches errors before push.

## Commit-time agent docs workflow (recommended)

- On every commit that changes code, run a docs-checker to ensure documentation and intent are kept in sync as the project grows.
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



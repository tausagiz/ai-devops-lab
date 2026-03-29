# AGENTS

This file summarizes guidance for AI agents ingesting this repository.

## Purpose

- DevOps learning project: automated Docker lifecycle with Python.
- Avoid rewrites of business logic; focus on build/run/log management.

## How to use for agents

1. Read `README.md` for overall intent and usage.
2. Process `main.py` for exact command behavior:
   - `build` => `myapp:latest` image build
   - `run` => detached container
   - `logs` => get logs from first container
   - `clean` => stop+remove all containers
3. Process `Dockerfile` for base image and default runtime behavior.

## GitHub Copilot

- Copilot can leverage this file plus repo contents.
- No duplication is needed; link agent behavior from here.
- Recommend adding `.github/copilot.yml` for custom assistant instructions (optional).

## Commit-time agent docs workflow (recommended)

- On every commit that changes code, run a docs-checker to ensure documentation and intent are kept in sync as the project grows.
- Suggested script pattern (generic):
  1. `diff` changed files.
  2. Identify changed behavior or public API (new features, flags, commands, interfaces).
  3. Verify documentation covers the changed behavior in `README.md`, `AGENTS.md`, and any dedicated docs files.
  4. For missing updates, fail with an actionable message (e.g., `docs: add new feature description to README/AGENTS`).

- Commit message template for agent-assisted writing:
  - `type(scope): concise summary` (e.g., `feat(docker): add restart workflow`)
  - body: 1) what changed, 2) why, 3) docs updated (README, AGENTS, etc.).

- CI/PR automation:
  - Add a GitHub Actions job to run `python scripts/check-docs.py` (or equivalent) on pull requests and pushes to `main`.
  - The workflow file is `.github/workflows/docs-check.yml` and it enforces commit message format + docs update requirement.
  - Optional: use Copilot to draft commit message and docs text for maintainers to review.



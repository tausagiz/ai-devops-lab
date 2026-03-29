# docker-automation

Automated Docker workflow helper for DevOps learning and practice.

This repository is built as a learning tool for DevOps skills. It shows a minimal Python-based approach to:
- building Docker images,
- running containers,
- checking logs,
- cleaning up containers.

## Repository structure

```
docker-automation/
├─ src/docker_automation/   # Python package (core logic)
│  ├─ cli.py                # CLI argument dispatch
│  ├─ config.py             # constants (IMAGE_TAG, BUILD_PATH)
│  ├─ docker_client.py      # Docker SDK client factory
│  └─ commands/             # one module per command
│     ├─ build.py
│     ├─ run.py
│     ├─ logs.py
│     └─ clean.py
├─ tests/
│  ├─ unit/                 # command-level unit tests (mocked Docker)
│  └─ integration/          # CLI smoke tests (no daemon required)
├─ scripts/
│  └─ check_docs.py         # CI docs + commit-message checker
├─ .github/workflows/
│  ├─ docs-check.yml
│  └─ tests.yml
├─ main.py                  # thin dev entry-point
├─ Dockerfile
├─ pyproject.toml
├─ requirements.txt
└─ requirements-dev.txt
```

## What this repo contains

- `src/docker_automation/cli.py` — dispatches `[build|run|logs|clean]` subcommands
- `src/docker_automation/commands/` — isolated handler per command
- `Dockerfile` — simple image based on `python:3.10-slim` with a default `echo`

## Prerequisites

- Docker engine running and accessible
- Python 3.10+

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"   # installs package + dev deps (pytest etc.)
```

> During development without `pip install`, `main.py` adds `src/` to `sys.path` automatically.

## Usage

```bash
python main.py build   # build myapp:latest image from current directory
python main.py run     # run container from built image (detached)
python main.py logs    # show logs from first running container
python main.py clean   # stop and remove all containers
```

After `pip install -e .` the installed CLI entry point is also available:

```bash
docker-automation build
```

## Testing

```bash
pytest tests/unit        # fast, no Docker daemon required
pytest tests/integration # CLI dispatch smoke tests
pytest tests/ --cov=docker_automation  # full coverage report
```

## Notes

- `build` tags image as `myapp:latest` (configured in `src/docker_automation/config.py`).
- `clean` stops and removes **all** containers on the host — use with care.

## Extend

- Add new command: create `src/docker_automation/commands/<name>.py` and register it in `cli.py`.
- Change image name or tag: edit `src/docker_automation/config.py`.
- Add `docker-compose` integration or restart workflow.

## AI agent-doc support

See [`AGENTS.md`](AGENTS.md) for AI-specific guidelines.

For faster commit preparation in VS Code chat, this repository also includes:

- `.github/agents/commit-coach.agent.md` — a custom Copilot agent that inspects git changes, validates docs-gate requirements, and can create the commit when the worktree is ready.
- `.github/prompts/prepare-commit.prompt.md` — a slash prompt for quickly invoking that end-to-end workflow from chat.

Example usage in VS Code chat:

```text
/Prepare Commit
/Prepare Commit add restart command and tests
```

The workflow is tailored to this repository's CI rules:

- commit titles must use the allowed Conventional Commit types,
- code changes should usually be committed together with a `README.md` or `AGENTS.md` update,
- the agent should either create the commit directly or stop with a concrete blocker,
- the agent should either create the commit directly or stop with a concrete blocker,
- the output includes a minimal validation step before push.

## CI checks

Two GitHub Actions workflows run on push to `main` and on pull requests:

- **`docs-check.yml`** — validates commit message format (Conventional Commits) and requires that `README.md` or `AGENTS.md` is updated when code changes are introduced.
- **`tests.yml`** — runs unit tests, integration tests, and coverage report.

Commit message format: `type(scope): summary`  
Allowed types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `build`, `ci`
- Changed files are detected from GitHub event SHAs for deterministic CI behavior:
  - pull request: `base.sha...head.sha`
  - push: `before..after`
  - with local and CI fallbacks when those values are unavailable.



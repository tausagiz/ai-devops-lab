# ai-devops-lab

A playground for exploring AI automation in DevOps workflows.

This repository is an experimental sandbox for DevOps learning and **AI-powered automation exploration**. It demonstrates how AI agents and tools can assist with:
- automating Docker image builds,
- running and managing containers programmatically,
- parsing container logs and diagnostics,
- orchestrating cleanup and lifecycle tasks.

It serves as a hands-on project for testing AI agents (like GitHub Copilot) in real DevOps scenarios.

## Repository structure

```
ai-devops-lab/
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
- AI-friendly structure: mocked Docker clients for testing, clear separation of concerns, and documented entry points for AI agents

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
ai-devops-lab build
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

## AI agent and developer support

See [`AGENTS.md`](AGENTS.md) for AI-specific guidelines and integration points.

For faster commit preparation in VS Code chat, this repository includes:

- `.github/agents/commit-coach.agent.md` — a custom Copilot agent that inspects git changes, validates docs-gate requirements, and can create compliant commits.

This repo is optimized for AI exploration: clean abstractions, testable code, and comprehensive documentation make it a good playground for testing how AI can improve DevOps workflows.

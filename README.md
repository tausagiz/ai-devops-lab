# ai-devops-lab

A low-risk sandbox for exploring AI automation in DevOps workflows.

This repository is optimized for cheap experimentation rather than production hardening. It is meant for comparing AI assistants, agent workflows, and automation tools with minimal risk, especially when working with free-tier limits or paid systems where prompt size, tool calls, and repeated context all cost money.

## Sandbox model

- Low operational risk: this repo is for learning and workflow experiments, not production deployment.
- Cost matters: prefer short prompts, small diffs, cheap local checks, and incremental validation.
- Free-tier friendly: mocked Docker usage and smoke tests make it practical to evaluate many tools without burning quotas.
- Compact by design: instructions are intentionally short to reduce token usage and repeated context loading.

## Repository structure

```text
ai-devops-lab/
|- src/docker_automation/   # core package
|  |- cli.py                # CLI dispatch
|  |- config.py             # constants
|  |- docker_client.py      # Docker SDK client factory
|  `- commands/             # build/run/logs/clean handlers
|- tests/
|  |- unit/                 # mocked Docker tests
|  `- integration/          # CLI smoke tests
|- scripts/
|  `- check_docs.py         # docs + commit-message checker
|- .github/
|  |- agents/               # GitHub Copilot workflow wrappers
|  `- prompts/              # Copilot slash-command entry points
|- main.py                  # thin dev entry point
|- Dockerfile
|- pyproject.toml
|- requirements.txt
`- requirements-dev.txt
```

## Prerequisites

- Docker engine running and accessible.
- Python 3.10+.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

> During development without `pip install`, `main.py` adds `src/` to `sys.path` automatically.

## Usage

```bash
python main.py build
python main.py run
python main.py logs
python main.py clean
```

After `pip install -e .`, you can also run:

```bash
ai-devops-lab build
```

## Testing

```bash
pytest tests/unit
pytest tests/integration
pytest tests/ --cov=docker_automation
```

Use the first two commands for the default cheap validation loop. Run coverage only when you explicitly need broader signal.

## Notes

- `build` tags the image as `myapp:latest` in `src/docker_automation/config.py`.
- `clean` stops and removes all containers on the host, so treat it as a sandbox command.
- Add new commands in `src/docker_automation/commands/` and register them in `cli.py`.

## Agent workflow support

Repository-wide policy lives in `AGENTS.md` and is intentionally provider-neutral.

Current GitHub Copilot integration lives in `.github/agents/` and `.github/prompts/`. Those files stay thin and mainly provide Copilot-specific entry points such as slash commands, argument hints, and output format.

Recommended VS Code workflow:

1. Run `/New Branch` to start work from updated `main`.
2. Implement the change.
3. Run `/Validate Changes` for fast local checks.
4. Run `/Prepare Commit` to create a compliant commit.
5. Run `/Open PR` to sync, validate, push, and open the PR.
6. Run `/Close Branch` after merge.

This keeps the repository easy to test across assistants while keeping token and tool usage low.

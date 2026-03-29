# ai-devops-lab

**Vendor-neutral agent design patterns for cost-conscious, AI-assisted development.**

A multi-experiment sandbox for exploring AI automation workflows. Current experiment: Docker automation CLI (more experiments planned). The repository's real value is twofold: a reusable vendor-neutral pattern and transparent sharing of practical lessons learned while applying it.

### The Core Problem This Solves

When you're working with AI assistants (especially free-tier or quota-limited), you face three challenges:

1. **Instruction duplication**: Agent policies are rewritten for GitHub Copilot, Claude, OpenAI, etc.—each tool gets its own verbatim copies.
2. **Token waste**: Repeated context loading and verbose instructions consume quotas quickly.
3. **Tool lock-in**: Switch AI tools? Rewrite all your agent instructions.

### The Solution

This repository demonstrates a **central policy + thin adapters** approach:

- **`AGENTS.md`** (vendor-neutral): *Single source of truth* for workflow policy, conventions, and agent behavior.
- **`.github/agents/` & `.github/prompts/`** (tool-specific): *Thin wrappers* that translate the central policy to tool-specific format (Copilot slash commands, Claude prompts, etc.).
- **Result**: 66% instruction reduction, portable workflows, free-tier friendly.

The Docker CLI is a *working experiment*—the real value is learning the pattern, then applying it to your own workflows or experiments.

## Design Philosophy

- **Low operational risk**: Sandbox for learning and experiments, not production.
- **Cost-conscious**: Mocked testing (~0 infrastructure cost), cheap-first validation (~2 seconds), free-tier compatible.
- **Token-efficient**: Central policy, no duplication, intentionally concise.
- **Portable**: Same workflows across GitHub Copilot, Claude, future tools, or even human teams.

## Repository Structure

Key files for understanding the pattern (and current experiments):

```text
ai-devops-lab/
|- AGENTS.md                          # ⭐ Core: Vendor-neutral policy (framework)
|- README.md                          # User guide (this file)
|- .github/
|  |- agents/                         # Copilot-specific agent wrappers
|  |- prompts/                        # Copilot slash-command entry points
|  `- workflows/                      # CI/CD validation
|
|- [EXPERIMENTS]
|  |
|  `- src/docker_automation/          # Experiment 1: Docker CLI automation
|     |- cli.py                       # Generic command dispatch pattern
|     |- config.py                    # How-to: centralize constants
|     |- docker_client.py             # How-to: dependency injection
|     `- commands/                    # How-to: modular extensibility
|  |
|- tests/                             # Testing strategy (applies to all experiments)
|  |- unit/                           # Mocked unit tests (no infrastructure)
|  `- integration/                    # CLI dispatch smoke tests
|- scripts/
|  `- check_docs.py                   # Documentation-as-code enforcement (shared)
|- main.py                            # Dev entry point
|- pyproject.toml                     # Package config
`- Dockerfile                         # Current experiment only
```

**`AGENTS.md` is the framework**: Experiments (in `src/`) demonstrate how to implement it. Want to adopt this pattern? Start with `AGENTS.md`. Want to understand patterns? Read the Docker experiment.

## Quick Start

```bash
git clone https://github.com/tausagiz/ai-devops-lab.git
cd ai-devops-lab
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

## Understanding the Agent Pattern (AGENTS.md)

`AGENTS.md` defines:
- **Repository character**: What this project is and isn't
- **Work priorities**: Cheap checks first, expensive validation on request
- **Workflow steps**: `/New Branch` → `/Validate` → `/Prepare Commit` → `/Open PR`
- **Conventions**: Branch naming, commit message format, docs requirements
- **Guardrails**: When to ask for confirmation, safety checks, risk mitigation

This file is **provider-neutral**—use it as-is with GitHub Copilot, or adapt for Claude, OpenAI, or any tool that reads markdown.

### How Tool Adapters Work

`.github/agents/` and `.github/prompts/` provide Copilot-specific syntax (slash commands, formatting hints). They **reference AGENTS.md rather than duplicating it**. Result: one policy update applies everywhere.

To add support for a new AI tool:
1. Read `AGENTS.md` to understand the workflows
2. Create a thin wrapper (tool-specific syntax)
3. Reference `AGENTS.md` from the wrapper
4. Done—no policy rewriting needed

## Current Experiment: Docker Automation CLI

The first experiment is a **Docker automation CLI**. It demonstrates:

- **Testability patterns**: Dependency injection, mocking, factory pattern
- **CLI design**: Clean dispatch, error handling, user feedback
- **Documentation-as-code**: Automated docs gates (`check_docs.py`)
- **Cheap validation**: Unit + integration tests require zero infrastructure

The Docker CLI is intentionally simple so the patterns stay visible. It's **not** the point—it's a vehicle for learning the pattern you can apply to build other experiments.

### Example: Running the Docker Commands

If Docker is installed and running:

```bash
python main.py build   # Build image from Dockerfile
python main.py run     # Start container in background
python main.py logs    # Fetch container logs
python main.py clean   # Stop and remove containers managed by this project
```

After `pip install -e .`, use the CLI directly:

```bash
ai-devops-lab build
```

> Note: `run` labels containers as managed by this project, and `clean`/`logs` target only those labeled containers.

### Testing the Example

The testing strategy reflects the repo's cost-conscious philosophy:

```bash
# Cheap validation (< 2 seconds, no infrastructure needed)
pytest tests/unit
pytest tests/integration
python scripts/check_docs.py

# Detailed analysis (optional, run on demand)
pytest tests/ --cov=docker_automation
```

**How it's cheap**: All Docker API calls are mocked. Unit tests don't require a running daemon. This makes CI/CD validation fast and free-tier compatible.

Note: `scripts/check_docs.py` resolves paths from the repository root, so it can be run from any working directory.

**Test structure**:
- `tests/unit/`: Command logic, error handling, output formatting (mocked Docker SDK)
- `tests/integration/`: CLI dispatch verification (mocked commands)

## Agent Workflows in Action

The workflow system defined in `AGENTS.md` works for any experiment. Here's an example using the Docker CLI:

### Recommended VS Code + Copilot Workflow (Docker Example)

If you have GitHub Copilot installed:

```
/New Branch "add push-command"
  ↓
# Edit src/docker_automation/commands/push.py (or any experiment)
# Update cli.py registration
# Add tests in tests/unit/ and tests/integration/
  ↓
/Validate Changes
  ↓
/Prepare Commit
  ↓
/Open PR
  ↓
# Review & merge on GitHub
  ↓
/Close Branch
```

Each slash command follows `AGENTS.md`: cheap checks first, clear errors, human confirmation for risky operations.

**Same workflow works for any experiment**: Replace Docker commands with your own CLI, API client, or infrastructure tool—the pattern stays the same.

### Adapting for Other AI Tools

The workflow system is **tool-agnostic**. To use with Claude, OpenAI, or any AI assistant:

1. Read `AGENTS.md` (vendor-neutral policy)
2. Translate slash commands to your tool's interaction model
3. Reference `AGENTS.md` from tool-specific instructions (no duplication)

Example: Claude doesn't have slash commands, but you can create a system prompt that references the same workflows and conventions from `AGENTS.md`.

## Key Files for Learning

| Goal | Start Here | What You'll Learn |
|------|-----------|-------------------|
| **Understand the framework** | `AGENTS.md` (vendor-neutral policy) | The reusable pattern for any experiment |
| **See tool integration** | `.github/agents/*.md`, `.github/prompts/*.md` | How to adapt policy to different AI tools |
| **Learn testing patterns** | `tests/unit/`, `tests/integration/` | How to mock and test without infrastructure (applies to any CLI) |
| **Understand CLI architecture** | `src/docker_automation/` (Docker experiment) | Command dispatch, factory pattern, dependency injection |
| **See docs enforcement** | `scripts/check_docs.py` | Documentation-as-code validation (shared across experiments) |
| **Build a new experiment** | Copy `src/docker_automation/` structure, replace `docker_automation` → your domain name | Adapt the pattern to your own CLI/automation tool |

## Use Cases

- 🎓 **Learning**: Study the pattern (`AGENTS.md`) → see it in action (Docker CLI) → build your own experiment
- 🔬 **Experimentation**: Test AI assistants fairly with consistent structure and automated workflows across multiple experiments
- 🏗️ **Adoption**: Adapt `AGENTS.md` framework for your own projects, teams, or workflows
- 🤝 **Collaboration**: Reference implementation for AI-assisted development, extensible by design

## Why This Pattern Matters

**Traditional approach**: Build a tool with embedded policy → lock into one AI tool → rewrite when switching tools.

**This approach**: Separate framework from tool → change AI tools without touching policy → reuse framework for different experiments.

Cost comparison:

| Dimension | Traditional | Framework-based |
|-----------|-----------|-----------------|
| Single tool | 1 policy | 1 policy |
| Two tools | 2 policies (100% duplication) | 1 policy + 2 adapters (66% reduction) |
| Three tools | 3 policies (200% duplication) | 1 policy + 3 adapters (80% reduction) |
| New experiment | Start from scratch | Copy framework, adapt domain |

**Free-tier friendly**: Test validation runs without infrastructure, without quotas, without cost. Perfect for comparing tools without burning tokens.

## Feedback and Project Boundaries

This repository is maintained primarily as a personal practice environment.

- Use **Issues/Discussions** to share feedback, observations, and suggestions.
- If you reuse ideas in your own fork, sharing outcomes back (what worked, what failed, and why) is strongly encouraged.
- If you want to implement ideas directly, you are welcome to **reuse the project in your own fork** under the repository license.
- The main collaboration model in this repository is discussion-first feedback focused on learning outcomes and knowledge transfer.

For contributor-facing guidance, see `CONTRIBUTING.md`.
For agent workflow and automation rules, see `AGENTS.md`.

Community adapters are intentionally thin:
- `CODE_OF_CONDUCT.md` defines collaboration behavior expectations.
- `.github/ISSUE_TEMPLATE/` standardizes feedback submission.

These files complement `AGENTS.md` and avoid duplicating automation-specific rules.

## License & Attribution

MIT License — see [LICENSE](LICENSE) file.

Copyright © 2026 Mateusz Rusnak.

— Built as an educational sandbox. Questions? Open an issue or discussion.

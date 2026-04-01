# AGENTS

Short guide for agents working in this repository.

## Repository character

- Educational sandbox for Docker automation and AI workflow testing.
- Risk is intentionally very low: fast and cheap experiments are more important than production-hard process rigor.
- The repo is used to compare multiple tools, especially those with free limits or cost tied to tokens/calls.
- Instructions should stay short and non-duplicative to reduce context cost.

## Work priorities

- Prefer small, reversible changes and short validation loops.
- Start with the cheapest checks: `pytest tests/unit`, `pytest tests/integration`, then coverage or more expensive steps.
- Minimize context: read only needed files and avoid duplicating the same rules across many instructions.
- Do not overengineer; this repo is for experimentation.

## Token-efficiency policy

- Keep responses compact by default: report outcomes first, include only necessary detail, and avoid long explanations unless the user asks.
- Do not create extra Markdown/docs files, new tests, or helper scripts by default.
- If adding docs/tests/scripts could improve quality but is not explicitly requested, stop and ask for user confirmation first.
- Prefer editing existing files over introducing new files.
- Before running broader validation, heavy analysis, or multi-step refactors not explicitly requested, ask for confirmation and suggest the cheapest next check.

## Project map

- `src/docker_automation/cli.py` - CLI entry point and command routing.
- `src/docker_automation/config.py` - constants (`IMAGE_TAG`, `BUILD_PATH`).
- `src/docker_automation/docker_client.py` - `get_client()` factory.
- `src/docker_automation/commands/*.py` - command implementations.
- `tests/unit/` - unit tests (Docker SDK mocked).
- `tests/integration/` - CLI smoke tests.
- `scripts/check_docs.py` - commit message + docs gate validation.

## Repository rules

- Implementation: access Docker only through `get_client()`; keep constants in `config.py`; each new command must live in `commands/` and be registered in `cli.py`.
- Language: developers may chat in any language, but all repository artifacts must be in English (code, comments, docstrings, variable/function names, CLI messages, tests, documentation, commit/PR descriptions).
- Branches: create a new branch only from up-to-date `main`; dirty worktree blocks branch switching; format `type/short-slug`; allowed types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `build`, `ci`; slug lowercase, hyphen-separated, 2-4 meaningful words, no type duplication; when the task description is too generic, ask for clarification instead of guessing.
- Commits: only `/Prepare Commit` workflow may auto-create a commit; other workflows must not commit or push without explicit request; title format `type(scope): summary` or `type: summary`; docs gate for code changes requires `README.md` or `AGENTS.md`; docs-gate auto-fix is allowed only by staging already existing changes in those files; do not create new documentation content only to pass the gate; with mixed scope, stop and ask for confirmation.
- Validation and PR: by default run `pytest tests/unit`, `pytest tests/integration`, `python scripts/check_docs.py`; narrower scope only on explicit request and then clearly state what was skipped; full validation only on explicit request (`pytest tests/ --cov=docker_automation`); target PR to `main` by default; if branch is behind `main`, ask for `merge` or `rebase` unless preference is already explicit; before push, stop on dirty worktree and suggest `/Prepare Commit`; include extra PR context in the body.
- User confirmation guardrail: when a proposed action increases token/call usage or project surface (new files, broader tests, extra scripts, large documentation updates), ask for explicit confirmation before proceeding unless already requested.
- Branch closing: never delete `main` or `master`; delete only branches merged into `origin/main` unless user explicitly confirms risky operation; when merge state is uncertain or `-D` would be needed, stop and wait for confirmation; never force-push or force-delete without explicit request.

## Tooling integration

- `AGENTS.md` is the repo-neutral layer and the primary source of rules for any agent.
- Files in `.github/agents/` and `.github/prompts/` are thin wrappers for slash commands, `argument-hint`, and response format; kept minimal to preserve token budget.
- If a rule applies to the whole repo, keep it here; in Copilot files keep only what is necessary to run the workflow.

## Vendor-agnostic policy

- Prefer vendor-neutral conventions and references in shared instructions (for example `#file:AGENTS.md` as the canonical rule source for automation).
- Keep provider-specific capabilities (tool names, frontmatter keys, slash-command wiring, platform-only metadata) in provider-scoped wrapper files only.
- Provider-scoped files must stay minimal adapters and must not duplicate agent workflow policy from `AGENTS.md`.
- When adding or changing automation guidance, update the universal rule in `AGENTS.md` first, then reference it from tool/vendor-specific files.
- Design new instruction/tool structures so another tool can adopt the same universal base without rewriting agent workflow policy.

## Workflow prompts

- `/Workflow Help` - list available workflows.
- `/New Branch` - update `main` and create a feature branch.
- `/Validate Changes` - local tests + docs gate.
- `/Fix Validation` - diagnose and fix failed validation checks, then rerun impacted checks.
- `/Prepare Commit` - prepare and create commit.
- `/Open PR` - branch sync, validation, push, and PR opening.
- `/Close Branch` - close merged branch and return to `main`.

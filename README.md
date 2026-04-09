# ai-learning-lab

Universal sandbox for AI-assisted learning workflows and course experiments.

This repository is now learning-first. Previous Docker automation examples were intentionally retired so each new topic can be built in a dedicated course structure under `learning/`.

## Why This Repo Exists

- Keep a lightweight place for practical AI-assisted learning.
- Compare workflows across tools with low operational overhead.
- Capture reusable patterns in one place without vendor lock-in.

## Repository Structure

```text
ai-learning-lab/
|- AGENTS.md
|- README.md
|- learning/
|  |- course-index.md
|  `- courses/
|- .github/
|  |- agents/
|  |- prompts/
|  |- instructions/
|  `- workflows/
|- scripts/
|  `- check_docs.py
|- tests/
|  |- unit/
|  `- integration/
|- requirements.txt
|- requirements-dev.txt
`- pyproject.toml
```

## Quick Start

```bash
git clone https://github.com/tausagiz/ai-learning-lab.git
cd ai-learning-lab
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

## Working Model

- Use `AGENTS.md` as the central, vendor-neutral workflow policy.
- Keep adapter files in `.github/agents/` and `.github/prompts/` thin and focused.
- Add new course-specific code in isolated folders when needed, instead of growing one monolithic example.

## Validation

Default low-cost checks:

```bash
python scripts/check_docs.py
```

## Roadmap

### Current Focus

- [ ] Establish baseline course skeleton templates in `learning/courses/`.

### Next Up

- [ ] Add first universal course module independent of Docker/DevOps.
- [ ] Add a lightweight checklist for course structure quality.

### Backlog

- [ ] Add optional examples for selected domains as separate course tracks.
- [ ] Add reusable course metadata conventions.

### Done Recently

- [x] Retired legacy Docker automation example to keep the repository learning-first.

## License

MIT License - see `LICENSE`.

Copyright © 2026 Mateusz Rusnak.

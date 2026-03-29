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

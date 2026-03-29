# docker-automation

Automated Docker workflow helper for DevOps learning and practice.

This repository is built as a learning tool for DevOps skills. It shows a minimal Python-based approach to:
- building Docker images,
- running containers,
- checking logs,
- cleaning up containers.

## What this repo contains

- `main.py` - command-line wrapper around `docker-py` (`docker` Python SDK)
  - `build` - builds image from current dir with `myapp:latest`
  - `run` - starts container from `myapp:latest` detached
  - `logs` - prints logs from first running container
  - `clean` - stops + removes all containers (all states)
- `Dockerfile` - simple image based on `python:3.10-slim` with a default `echo`

## Prerequisites

- Docker engine running and accessible
- Python 3.10+ (recommended)
- Python virtual environment (optional, but recommended)

## Setup

```bash
cd /home/mateusz/docker-automation
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # or pip install docker
```

> If `requirements.txt` is not in repo yet, use:
> `pip install docker`

## Usage

```bash
python main.py build   # build image from current directory
python main.py run     # run container from built image
python main.py logs    # show container logs
python main.py clean   # stop/remove all containers
```

## Notes

- `build` command currently tags image as `myapp:latest`.
- `run` command uses this image and detaches (`-d`) without mapping ports.
- `logs` reads first container from `client.containers.list()`; adjust if multiple containers exist.
- `clean` is aggressive and removes all containers on host, use with care.

## Extend

- add explicit image name / tag options
- add container name, port mappings, volumes
- add `docker-compose` integration


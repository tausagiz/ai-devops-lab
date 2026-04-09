---
description: "Use when writing or reviewing Python source code in src/. Covers module structure, Docker client access, constants, and command registration."
applyTo: "src/**/*.py"
---
# Python Source Conventions

- Access Docker only through `get_client()` from `docker_automation.docker_client`; never instantiate `docker.DockerClient` directly.
- Keep all runtime constants (`IMAGE_TAG`, `BUILD_PATH`, label keys) in `config.py`; import from there in every other module.
- Each new command lives in its own file under `src/docker_automation/commands/` and must be registered in `cli.py`'s `_commands()` map.
- Command functions use `-> None` return type; print status with emoji prefix (`🔨`, `✅`, `❌`) for consistency with existing commands.
- Catch exceptions broadly (`except Exception as e`) inside command functions, print the error, and call `sys.exit(1)` on failure.
- No docstrings required on private helpers; keep module-level comments minimal.

---
description: "Use when writing or reviewing tests in tests/unit/ or tests/integration/. Covers mock patterns, assertion style, and test structure."
applyTo: "tests/**/*.py"
---
# Testing Conventions

## Unit tests (`tests/unit/`)
- Mock Docker client via `patch("docker_automation.commands.<module>.get_client")`.
- Use `MagicMock()` for container/image objects; configure return values inline in the `with patch(...)` block.
- Capture printed output with `capsys`; assert on substrings (`assert "Expected text" in out`), not exact strings.
- Use `pytest.raises(SystemExit)` to assert `sys.exit(1)` on error paths; check `exc_info.value.code == 1`.
- One test file per command module; name pattern `test_<command>.py`.

## Integration tests (`tests/integration/`)
- CLI smoke tests only; keep them thin — verify the command is reachable and exits cleanly, not detailed behaviour.

## General
- No fixtures file (`conftest.py`) unless shared fixtures are needed by 3+ tests.
- Import the function under test directly; do not test via `subprocess` in unit tests.
- Keep test names descriptive: `test_<function>_<scenario>` (e.g., `test_build_image_success`).

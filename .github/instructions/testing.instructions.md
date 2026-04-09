---
description: "Use when writing or reviewing tests in tests/unit/ or tests/integration/. Covers assertion style, mocks, and test structure for course modules."
applyTo: "tests/**/*.py"
---
# Testing Conventions

## Unit tests (`tests/unit/`)
- Mock external boundaries at module level using `patch("<module>.<dependency>")`.
- Use `MagicMock()` for collaborator objects; configure return values inline in the test scope.
- Capture printed output with `capsys`; assert on substrings (`assert "Expected text" in out`), not exact strings.
- Use `pytest.raises(SystemExit)` to assert `sys.exit(1)` on error paths; check `exc_info.value.code == 1`.
- Keep one test file per feature module; use `test_<feature>.py` naming.

## Integration tests (`tests/integration/`)
- Keep integration tests thin: verify module wiring and key flows, not exhaustive edge behavior.

## General
- No fixtures file (`conftest.py`) unless shared fixtures are needed by 3+ tests.
- Import the function under test directly; do not test via `subprocess` in unit tests.
- Keep test names descriptive: `test_<function>_<scenario>` (e.g., `test_build_image_success`).

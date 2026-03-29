"""Smoke tests for CLI argument dispatch — no Docker daemon required."""
import sys
from unittest.mock import patch

import pytest

from docker_automation.cli import main

_DISPATCH_CASES = [
    ("build", "docker_automation.commands.build.build_image"),
    ("run", "docker_automation.commands.run.run_container"),
    ("logs", "docker_automation.commands.logs.show_logs"),
    ("clean", "docker_automation.commands.clean.cleanup"),
]


@pytest.mark.parametrize("command,target", _DISPATCH_CASES)
def test_cli_dispatches_to_correct_function(command, target, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py", command])
    with patch(target) as mock_fn:
        main()
    mock_fn.assert_called_once()


def test_cli_no_args_exits_with_usage(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1
    assert "Usage" in capsys.readouterr().out


def test_cli_unknown_command_exits(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "restart"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1
    assert "Unknown command" in capsys.readouterr().out

from unittest.mock import MagicMock, patch

import pytest

from docker_automation.commands.clean import cleanup
from docker_automation.config import MANAGED_LABEL_FILTER


def test_cleanup_stops_and_removes_matching_containers(capsys):
    mock_c1, mock_c2 = MagicMock(), MagicMock()

    with patch("docker_automation.commands.clean.get_client") as mock_get_client:
        mock_get_client.return_value.containers.list.return_value = [mock_c1, mock_c2]

        cleanup()

        mock_get_client.return_value.containers.list.assert_called_once_with(
            all=True,
            filters={"label": MANAGED_LABEL_FILTER},
        )
        for c in (mock_c1, mock_c2):
            c.stop.assert_called_once()
            c.remove.assert_called_once()
        assert "Done" in capsys.readouterr().out


def test_cleanup_no_matching_containers(capsys):
    with patch("docker_automation.commands.clean.get_client") as mock_get_client:
        mock_get_client.return_value.containers.list.return_value = []

        cleanup()

        assert "No managed project containers found" in capsys.readouterr().out


def test_cleanup_exception_exits_with_error(capsys):
    with patch("docker_automation.commands.clean.get_client") as mock_get_client:
        mock_get_client.return_value.containers.list.side_effect = Exception("Docker daemon not running")

        with pytest.raises(SystemExit) as exc_info:
            cleanup()

        assert exc_info.value.code == 1
        assert "Docker daemon not running" in capsys.readouterr().out

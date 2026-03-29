from unittest.mock import MagicMock, patch

import pytest

from docker_automation.commands.run import run_container


def test_run_container_success(capsys):
    mock_container = MagicMock()
    mock_container.short_id = "abc123"

    with patch("docker_automation.commands.run.get_client") as mock_get_client:
        mock_get_client.return_value.containers.run.return_value = mock_container

        run_container()

        mock_get_client.return_value.containers.run.assert_called_once_with("myapp:latest", detach=True)
        assert "abc123" in capsys.readouterr().out


def test_run_container_failure(capsys):
    with patch("docker_automation.commands.run.get_client") as mock_get_client:
        mock_get_client.return_value.containers.run.side_effect = Exception("Image not found")

        with pytest.raises(SystemExit) as exc_info:
            run_container()

        assert exc_info.value.code == 1
        assert "Image not found" in capsys.readouterr().out

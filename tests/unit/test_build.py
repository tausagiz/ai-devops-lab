from unittest.mock import MagicMock, patch

import pytest

from docker_automation.commands.build import build_image


def test_build_image_success(capsys):
    mock_image = MagicMock()
    mock_logs = [{"stream": "Step 1/1 : FROM python:3.10-slim\n"}, {"stream": "Successfully built abc123\n"}]

    with patch("docker_automation.commands.build.get_client") as mock_get_client:
        mock_get_client.return_value.images.build.return_value = (mock_image, iter(mock_logs))

        build_image()

        mock_get_client.return_value.images.build.assert_called_once_with(path=".", tag="myapp:latest")
        out = capsys.readouterr().out
        assert "Step 1/1" in out
        assert "Image built" in out


def test_build_image_failure(capsys):
    with patch("docker_automation.commands.build.get_client") as mock_get_client:
        mock_get_client.return_value.images.build.side_effect = Exception("Connection refused")

        with pytest.raises(SystemExit) as exc_info:
            build_image()

        assert exc_info.value.code == 1
        assert "Connection refused" in capsys.readouterr().out

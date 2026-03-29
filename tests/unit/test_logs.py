from unittest.mock import MagicMock, patch

from docker_automation.commands.logs import show_logs


def test_show_logs_success(capsys):
    mock_container = MagicMock()
    mock_container.logs.return_value = b"log line 1\nlog line 2\n"

    with patch("docker_automation.commands.logs.get_client") as mock_get_client:
        mock_get_client.return_value.containers.list.return_value = [mock_container]

        show_logs()

        out = capsys.readouterr().out
        assert "log line 1" in out
        assert "log line 2" in out


def test_show_logs_no_running_containers(capsys):
    with patch("docker_automation.commands.logs.get_client") as mock_get_client:
        mock_get_client.return_value.containers.list.return_value = []

        show_logs()

        assert "No running containers" in capsys.readouterr().out


def test_show_logs_unexpected_exception(capsys):
    with patch("docker_automation.commands.logs.get_client") as mock_get_client:
        mock_get_client.return_value.containers.list.side_effect = Exception("Socket error")

        show_logs()

        assert "Socket error" in capsys.readouterr().out

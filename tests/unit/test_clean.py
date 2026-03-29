from unittest.mock import MagicMock, patch

from docker_automation.commands.clean import cleanup


def test_cleanup_stops_and_removes_all_containers(capsys):
    mock_c1, mock_c2 = MagicMock(), MagicMock()

    with patch("docker_automation.commands.clean.get_client") as mock_get_client:
        mock_get_client.return_value.containers.list.return_value = [mock_c1, mock_c2]

        cleanup()

        mock_get_client.return_value.containers.list.assert_called_once_with(all=True)
        for c in (mock_c1, mock_c2):
            c.stop.assert_called_once()
            c.remove.assert_called_once()
        assert "Done" in capsys.readouterr().out


def test_cleanup_no_containers(capsys):
    with patch("docker_automation.commands.clean.get_client") as mock_get_client:
        mock_get_client.return_value.containers.list.return_value = []

        cleanup()

        assert "Done" in capsys.readouterr().out


def test_cleanup_exception(capsys):
    with patch("docker_automation.commands.clean.get_client") as mock_get_client:
        mock_get_client.return_value.containers.list.side_effect = Exception("Docker daemon not running")

        cleanup()

        assert "Docker daemon not running" in capsys.readouterr().out

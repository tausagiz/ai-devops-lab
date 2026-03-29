import sys


def _commands() -> dict:
    """Build command map freshly each call so unit tests can patch command modules."""
    from docker_automation.commands.build import build_image
    from docker_automation.commands.clean import cleanup
    from docker_automation.commands.logs import show_logs
    from docker_automation.commands.run import run_container

    return {
        "build": build_image,
        "run": run_container,
        "logs": show_logs,
        "clean": cleanup,
    }


def main() -> None:
    commands = _commands()

    if len(sys.argv) < 2:
        print(f"Usage: python main.py [{' | '.join(commands)}]")
        sys.exit(1)

    command = sys.argv[1]
    handler = commands.get(command)

    if handler is None:
        print(f"❌ Unknown command: {command!r}")
        print(f"Available commands: {', '.join(commands)}")
        sys.exit(1)

    handler()

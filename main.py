"""Entry point for development use.

For direct execution: python main.py [build|run|logs|clean]
After `pip install -e .` the `ai-devops-lab` CLI command is also available.
"""
import os
import sys

# Allow running without `pip install -e .` during development.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from docker_automation.cli import main  # noqa: E402

if __name__ == "__main__":
    main()
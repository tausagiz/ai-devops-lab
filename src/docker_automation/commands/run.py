import sys

from docker_automation.config import IMAGE_TAG
from docker_automation.docker_client import get_client


def run_container() -> None:
    print("🚀 Starting container...")
    try:
        client = get_client()
        container = client.containers.run(IMAGE_TAG, detach=True)
        print(f"Container running: {container.short_id}")
    except Exception as e:
        print(f"❌ Error starting container: {e}")
        sys.exit(1)

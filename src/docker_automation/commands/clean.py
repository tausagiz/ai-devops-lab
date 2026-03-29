import sys

from docker_automation.config import MANAGED_LABEL_FILTER
from docker_automation.docker_client import get_client


def cleanup() -> None:
    print("🧹 Cleaning...")
    try:
        client = get_client()
        containers = client.containers.list(all=True, filters={"label": MANAGED_LABEL_FILTER})
        if not containers:
            print("ℹ️ No managed project containers found.")
            return

        for container in containers:
            container.stop()
            container.remove()
        print("🧼 Done.")
    except Exception as e:
        print(f"❌ Error during cleanup: {e}")
        sys.exit(1)

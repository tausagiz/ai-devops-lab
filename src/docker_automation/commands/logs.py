import sys

from docker_automation.config import MANAGED_LABEL_FILTER
from docker_automation.docker_client import get_client


def show_logs() -> None:
    print("📜 Container logs:")
    try:
        client = get_client()
        containers = client.containers.list(all=False, filters={"label": MANAGED_LABEL_FILTER})
        if not containers:
            print("❌ No running managed project containers.")
            return

        print(containers[0].logs().decode())
    except Exception as e:
        print(f"❌ Error fetching logs: {e}")
        sys.exit(1)

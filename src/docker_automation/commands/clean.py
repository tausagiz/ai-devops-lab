from docker_automation.docker_client import get_client


def cleanup() -> None:
    print("🧹 Cleaning...")
    try:
        client = get_client()
        for container in client.containers.list(all=True):
            container.stop()
            container.remove()
        print("🧼 Done.")
    except Exception as e:
        print(f"❌ Error during cleanup: {e}")

from docker_automation.docker_client import get_client


def show_logs() -> None:
    print("📜 Container logs:")
    try:
        client = get_client()
        container = client.containers.list()[0]
        print(container.logs().decode())
    except IndexError:
        print("❌ No running containers.")
    except Exception as e:
        print(f"❌ Error fetching logs: {e}")

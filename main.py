import docker
import sys

client = docker.from_env()

def build_image():
    print("🔨 Building image...")
    try:
        image, logs = client.images.build(path=".", tag="myapp:latest")
        for line in logs:
            print(line.get("stream", ""), end="")
        print("✅ Image built.")
    except Exception as e:
        print(f"❌ Error building image: {e}")
        sys.exit(1)

def run_container():
    print("🚀 Starting container...")
    try:
        container = client.containers.run("myapp:latest", detach=True)
        print(f"Container running: {container.short_id}")
    except Exception as e:
        print(f"❌ Error starting container: {e}")
        sys.exit(1)

def show_logs():
    print("📜 Container logs:")
    try:
        container = client.containers.list()[0]
        print(container.logs().decode())
    except IndexError:
        print("❌ No running containers.")
    except Exception as e:
        print(f"❌ Error fetching logs: {e}")

def cleanup():
    print("🧹 Cleaning...")
    try:
        for container in client.containers.list(all=True):
            container.stop()
            container.remove()
        print("🧼 Done.")
    except Exception as e:
        print(f"❌ Error during cleanup: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [build|run|logs|clean]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "build":
        build_image()
    elif command == "run":
        run_container()
    elif command == "logs":
        show_logs()
    elif command == "clean":
        cleanup()
    else:
        print(f"Unknown command: {command}")
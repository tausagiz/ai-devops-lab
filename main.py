import docker
import sys

client = docker.from_env()

def build_image():
    print("🔨 Buduję obraz...")
    try:
        image, logs = client.images.build(path=".", tag="myapp:latest")
        for line in logs:
            print(line.get("stream", ""), end="")
        print("✅ Obraz zbudowany.")
    except Exception as e:
        print(f"❌ Błąd podczas budowania obrazu: {e}")
        sys.exit(1)

def run_container():
    print("🚀 Uruchamiam kontener...")
    try:
        container = client.containers.run("myapp:latest", detach=True)
        print(f"Kontener działa: {container.short_id}")
        return container
    except Exception as e:
        print(f"❌ Błąd podczas uruchamiania kontenera: {e}")
        sys.exit(1)

def show_logs(container):
    print("📜 Logi kontenera:")
    print(container.logs().decode())

def cleanup(container):
    print("🧹 Czyszczenie...")
    container.stop()
    container.remove()
    print("🧼 Gotowe.")

if __name__ == "__main__":
    build_image()
    container = run_container()
    show_logs(container)
    cleanup(container)
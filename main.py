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
    except Exception as e:
        print(f"❌ Błąd podczas uruchamiania kontenera: {e}")
        sys.exit(1)

def show_logs():
    print("📜 Logi kontenera:")
    try:
        container = client.containers.list()[0]
        print(container.logs().decode())
    except IndexError:
        print("❌ Brak działających kontenerów.")
    except Exception as e:
        print(f"❌ Błąd podczas pobierania logów: {e}")

def cleanup():
    print("🧹 Czyszczenie...")
    try:
        for container in client.containers.list(all=True):
            container.stop()
            container.remove()
        print("🧼 Gotowe.")
    except Exception as e:
        print(f"❌ Błąd podczas czyszczenia: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: python main.py [build|run|logs|clean]")
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
        print(f"Nieznana komenda: {command}")
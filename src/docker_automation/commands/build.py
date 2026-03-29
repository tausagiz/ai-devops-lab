import sys

from docker_automation.config import BUILD_PATH, IMAGE_TAG
from docker_automation.docker_client import get_client


def build_image() -> None:
    print("🔨 Building image...")
    try:
        client = get_client()
        image, logs = client.images.build(path=BUILD_PATH, tag=IMAGE_TAG)
        for line in logs:
            print(line.get("stream", ""), end="")
        print("✅ Image built.")
    except Exception as e:
        print(f"❌ Error building image: {e}")
        sys.exit(1)

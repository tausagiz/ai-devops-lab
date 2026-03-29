import docker


def get_client() -> docker.DockerClient:
    """Return a Docker client connected to the local daemon via the default socket."""
    return docker.from_env()

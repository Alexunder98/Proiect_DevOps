import docker
import sys

client = docker.from_env()

# Get the image name and command from the command line arguments
image_name = sys.argv[1]
command = sys.argv[2:]

# Start a new container using the image and command
container = client.containers.run(image_name, command)

# Print the container logs
print(container.decode())

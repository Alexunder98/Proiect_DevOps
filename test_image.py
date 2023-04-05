import docker
import sys

client = docker.from_env()

# Get the image name and Dockerfile path from the command line arguments
# image_name = sys.argv[1]
# dockerfile_path = sys.argv[2]
# path=dockerfile_path, tag=image_name
# Build the Docker image using the image name and Dockerfile path
image, build_logs = client.images.build(sys.argv[1:])
# Print the ID of the built image
print("Built image:", image.id)
print(build_logs)
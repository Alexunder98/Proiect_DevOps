#!/usr/bin/python3

import subprocess, argparse, sys, requests, json, yaml


# ./pipeline.py build <arg1> <arg2> ...: builds the Docker image with the Flask application;
def image_build(imageName, imageTag, dockerFile):
    if imageName != None and imageTag != None and dockerFile != None:
        # docker build -t devschool:latest .
        docker_build = "docker build -t " + imageName + ":" + imageTag + " " + dockerFile    
        subprocess.run(docker_build, shell=True)
    else:
        print("Build command should have params: imageName, imageTag and dockerFile path")
    return


# ./pipeline.py push <arg1> <arg2> ...: pushes the created Docker image into a container registry;
def image_push(registryName, imageName, imageTag):
    # Login intro docker hub with your credentials
    subprocess.run("docker login", shell=True)
    if registryName != None and imageName != None and imageTag != None:
        # docker tag devschool:latest dorin123/devschool:latest
        # docker push dorin123/devschool:latest
        docker_tag = "docker tag " + imageName + ":" + imageTag + " " + registryName + "/" + imageName + ":" + imageTag
        docker_push = "docker push " + registryName + "/" + imageName + ":" + imageTag
        subprocess.run(docker_tag, shell = True)
        subprocess.run(docker_push, shell = True)
    else:
        print("Push command should have params: registryName, imageName, imageTag")
    return


# ./pipeline.py deploy <arg1> <arg2> ...: deploys a container with the Flask application on your local machine using Docker;
def image_deploy(imageName, imageTag):
    if imageTag != None and imageName != None:
        # docker container run -d -p 80:80 dorin123/devschool:latest
        docker_run = "docker container run -d -p 80:80 " + imageName + ":" + imageTag
        subprocess.run(docker_run, shell = True)
    else:
        print("Docker deploy should have imageName and imageTag")
    return


def get_test(endPoint):
    if endPoint != None:
        subprocess.run("curl -i " + endPoint, shell = True)
    else:
        print("Invalid end point")
    return


def k8s_deploy(imageName, imageTag, pathManifest):
    data = dict()

    with open(pathManifest, 'r') as f:
        data = yaml.safe_load(f)
        if data['kind'] == "Deployment":
            data['spec']['template']['spec']['containers'][0]['image'] = imageName + ":" + imageTag
    f.close()

    with open(pathManifest, 'w') as file:
        yaml.dump(data, file, sort_keys=False)
    file.close()

    subprocess.run("kubectl apply -f " + pathManifest, shell = True)
    return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", help="mandatory argument")
    parser.add_argument("--imageName", help="optional argument")
    parser.add_argument("--imageTag", help="optional argument")
    parser.add_argument("--dockerFilePath", help="optional argument")
    parser.add_argument("--containerRegistryUsername", help="optional argument")
    parser.add_argument("--flavour", help="optional argument")
    parser.add_argument("--endPoint", help="optional argument")
    parser.add_argument("--pathManifest", help="optional argument")
    params = parser.parse_args()

    if params.stage == "build":
        image_build(params.imageName, params.imageTag, params.dockerFilePath)
    elif params.stage == "push":
        image_push(params.containerRegistryUsername, params.imageName, params.imageTag)
    elif params.stage == "deploy" and params.flavour == "docker":
        image_deploy(params.imageName, params.imageTag)
    elif params.stage == "deploy" and params.flavour == "kubernetes":
        k8s_deploy(params.imageName, params.imageTag, params.pathManifest)
    elif params.stage == "test":
        get_test(params.endPoint)


if __name__ == "__main__":
    main()
    
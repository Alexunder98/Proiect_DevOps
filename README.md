# ING {DEV}School 2023 Final Project
## Authors
- [Alexunder98](https://github.com/Alexunder98)
- [Ciumac23](https://github.com/Ciumac23)
## Features

- FLASK app
- Python script
- Local Docker deploy using the python script
- Azure Cloud deploy uisng pipeline
- BONUS 1: Local Kubernetes Cluster deploy  

## Description

This is a DevOps project that involves the development of a Flask application with Docker, Kubernetes and Azure Devops. The application is capable of making REST requests to a public API and retrieving the response in JSON format. It also has the ability to parse the JSON response and includes a simple frontend using an HTML template.

To ensure the application can run consistently across different environments, a Dockerfile has been created. The Dockerfile builds an image that contains all the necessary components required for the app to run.

In addition to this, a Python script has been developed that enables Continuous Integration/Continuous Deployment (CI/CD) on a local machine. The script can build, push, deploy, and test the app based on the arguments provided during the call.

Lastly, the YAML pipeline in Azure DevOps builds, pushes, deploys and tests the Docker image with the Flask app to Azure Container Instances (ACI).   

As a bonus feature, a Kubernetes deployment has also been created for the Flask application. The deployment runs the application in a Kubernetes cluster that is deployed on a local machine.

Overall, this project provides a reliable and automated way to deploy a Flask web application using Docker containers and Azure Pipelines, enabling easy scalability and management of the application in a production environment.


### Flask App

This Flask web application interacts with two APIs: Star Wars API (swapi.dev) and Meme API (meme-api.com). The application has several endpoints, including one that returns a list of Star Wars characters as a JSON object, another that returns a single character based on the ID, and an endpoint to add, update, and delete a character. For the meme API there is an endpoint that returns a random meme image and subreddit name from the Meme API.  
The app also includes a liveness endpoint that serves to indicate that the application is currently operational.

### Dockerfile

The Dockerfile uses an Alpine-based Python 3 image as its base and creates a working directory **/app**. The contents of the local directory **./flask_app** are copied to **/app** inside the container. The required dependencies are installed using **pip** based on the **requirements.txt** file, and **port 80** is exposed. Finally, the command to start the Flask application is specified using CMD.

### Python Script

The Python script serves as a command-line interface for a pipeline used for building, pushing, and deploying the Flask application using Docker and Kubernetes on local. It has five possible stages of execution: build, push, deploy (either with Docker or Kubernetes), and test. It takes command-line arguments to specify the stage, image name and tag, Dockerfile path, container registry credentials, endpoint for testing, and path to the Kubernetes manifest. The script uses subprocess, argparse, sys, requests, json, and yaml Python modules to implement the functionality of the different stages.

### YAML Pipeline

It has four stages: Build, Push, Deploy, and Test.

In the Build stage, the Docker image is built using the Docker@2 task. The Dockerfile and the build context directory are provided as input. The Docker image is tagged using the *tag* variable.

In the Push stage, the Docker image is pushed to the container registry using the Docker@2 task. The image repository, container registry, and tag are provided as inputs.

In the Deploy stage, four tasks are performed. First, an Azure Key Vault is created. Then, the container registry's pull password and ID are stored in the key vault. Finally, a container instance is created in ACI using the image in the container registry. The container instance is assigned a public IP and a health check is performed on the /liveness endpoint of the web application.

In the Test stage, a Bash script sends a request to the /liveness endpoint of the container instance created in the Deploy stage. The request is sent 10 times, and if the response code is 200, the script declares the application to be live.

### App Homepage - Local

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/homepage.png"
  alt="App Homepage">
</p>

### Meme Page - Cloud

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/meme_cloud.png"
  alt="App Meme page">
</p>

### Azure Devops - Cloud deploy uisng pipeline

<p align="center"><img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/stages.png"></p>

<p align="center"><img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/Ci.png"></p>

<p align="center"><img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/liveness_test.png"></p>


#### DEMO: Local Docker deploy using the python script

- Build an image: `python3 pipeline.py build --imageName=<image-name> --imageTag=<image-tag> --dockerFilePath=<path>`

<p align="center"><img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/p1.png"></p>

- Push the image to docker hub: `python3 pipeline.py push --containerRegistryUsername=<registry-username> --imageName=<image-name> --imageTag=<image-tag>`

<p align="center"><img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/p2.png"></p>

- Image successfully uploaded to Docker Hub:
<p align="center"><img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/p3.png"></p>

- Deploy with Docker Hub: `python3 pipeline.py deploy --flavour=<docker> --imageName=<image-name> --imageTag=<image-tag>`

<p align="center"><img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/p4.png"></p>

- Liveness test: `python3 pipeline.py test --endPoint=<local-endpoint>`

<p align="center"><img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/p5.png"></p>

#### BONUS 1: Local Kubernetes Cluster deploy  

- Deploy local with k8s: `python3 pipeline.py deploy --flavour=<kubernetes> --imageName=<image-name> --imageTag=<image-tag> --pathManifest=<yaml-path>`

<p align="center"><img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/p6.png"></p>

#### DEMO: FLASK APP - GET, PUT, DELETE

- GET localhost/chars
<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/get_chars.png"></p>

- PUT localhost/chars/id
<p align="center"><img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/put_char.png"></p>

- DELETE localhost/chars/id
<p align="center"><img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/del_char.png"></p>

### Resources
- [ACR DEPLOY](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tutorial-quick-task)

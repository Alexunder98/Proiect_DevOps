# ING {DEV}School 2023 Final Project

## Features

- FLASK app
- Python script
- Local Docker deploy using the python script
- Azure Cloud deploy uisng pipeline
- BONUS 1: Local Kubernetes Cluster deploy  

### FLASK app
- _GET localhost/liveness_

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/get_liveness.png"
  width="640" height="360">
</p>

- _GET localhost/chars_

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/get_chars.png"
  width="640" height="360">
</p>

- _PUT localhost/chars/id_

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/put_char.png"
  width="640" height="360">
</p>

- _DELETE localhost/chars/id_

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/del_char.png"
  width="640" height="360">
</p>

### Python script
### Local Docker deploy using the python script
- Build an image
>`python3 pipeline.py build --imageName=<image-name> --imageTag=<image-tag> --dockerFilePath=<path>`

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/p1.png">
</p>

- Push the image to docker hub
>`python3 pipeline.py push --containerRegistryUsername=<registry-username> --imageName=<image-name> --imageTag=<image-tag>`

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/p2.png">
</p>
<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/p3.png">
</p>

- Deploy local with docker hub
>`python3 pipeline.py deploy --flavour=<docker> --imageName=<image-name> --imageTag=<image-tag>`

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/p4.png">
</p>

- Test local
>`python3 pipeline.py test --endPoint=<local-endpoint>`

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/p5.png">
</p>

### BONUS 1: Local Kubernetes Cluster deploy  

- Deploy local with k8s
>`python3 pipeline.py deploy --flavour=<kubernetes> --imageName=<image-name> --imageTag=<image-tag> --pathManifest=<yaml-path>`

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/p6.png">
</p>

### Azure Cloud deploy uisng pipeline

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/az1.png">
</p>

### App Homepage

<p align="center">
<img src="https://github.com/Alexunder98/Proiect_DevOps/blob/master/img/homepage.png"
  alt="App Homepage">
</p>

# Overview
In this project, we use semi-supervised learning to train a plant disease classifier in a lable efficient manner. Initially, we pretrained, and fine tuned the [simclrv2](https://github.com/google-research/simclr) architecture on the TFDS plant village dataset. Finally, we applied transfer learning to adapt the network for leaf pathology detection problem.

The leaf pathology dataset consists of classifying whether fruit trees and plants are experiencing an on-set of scab, rust or another combination of parasites (multiple diseases) leading to destruction of the garden.

Finally, we deployed the results in a leaf condition classification web application. Future extensions include deploying a mobile application for providing real-time classification to farmers, as well as expanding the scope of the classification task to include a wide array of leaves.

# Datasets
All datasets used, along with colabs used to download them are available [here](https://drive.google.com/drive/folders/1u9zDyzAc2CBjUM--RBDSqRt0pcj3o5gs?usp=sharing)

OASIS-1 dataset is available at [oasis-brains](http://oasis-brains.org/)

**Note**: You must be logged in with a @sjsu account to view the datasets Google Drive link.

# Web Application
Deployment [Link](http://34.94.186.33/)

**Note**: The Kubernetes pod used for web application deployment is rather small. Inference may take a long time (minutes)!

# Deployment
Continuous Deployment Pipeline is implemented via Github actions. Upon pushing a new version tag, the build is created, dockerized and pushed to a Kubernetes pod.

Previous pipeline runs can be viewed [here](https://github.com/manmeet3/Medical-SSL-SimCLRv2/actions?query=workflow%3A%22Build+and+Deploy+to+GKE%22)

`Deployment diagram is available at static/deployment.jpg`

## Working with dockerized web app
1. create container: `docker build -t clf-app:latest .`
        a. This will containarize the app from the WebApp folder, installing all dependencies
2. You can run the container using `docker run -p 5000:5000 clf-app:latest 
3. Accessing the container with bash: `docker run -it --entrypoint /bin/bash $image_id`
4. View container logs: `docker logs $containerid`
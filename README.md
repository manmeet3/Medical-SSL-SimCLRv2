# Medical-SSL-SimCLRv2

# Working with dockerized web app
1. create container: `docker build -t clf-app:latest .`
        a. This will create the app from the WebApp folder and install all dependencies
2. Accessing the container with bash: `docker run -it --entrypoint /bin/bash $image_id`
3. View container logs: `docker logs $containerid`

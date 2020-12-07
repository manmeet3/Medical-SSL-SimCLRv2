FROM ubuntu:20.04

MAINTAINER Manmeet Singh "manmeet3@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev vim curl libjpeg-dev zlib1g-dev

RUN pip3 install --upgrade pip

WORKDIR /app

COPY ./WebApp /app

RUN pip3 install -r /app/requirements.txt -t /app

ENTRYPOINT [ "python3" ]

CMD ["app.py"]

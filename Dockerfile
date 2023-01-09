FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Madrid

RUN apt-get -y update
RUN apt-get install git build-essential cmake python3 python3-dev python3-pip -y

RUN apt-get -y install git

COPY install_simplefhe_docker.py .
COPY scenario.py .

RUN python3 install_simplefhe_docker.py

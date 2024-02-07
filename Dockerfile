FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get upgrade -y
RUN apt-get update -y
RUN apt-get install python3 python3-pip libpq-dev -y
RUN apt-get install nginx -y

## ENVOY INSTALL

RUN apt-get update -y
RUN apt-get install apt-transport-https gnupg2 curl lsb-release -y
RUN curl -sL 'https://deb.dl.getenvoy.io/public/gpg.8115BA8E629CC074.key' | gpg --dearmor -o /usr/share/keyrings/getenvoy-keyring.gpg
RUN echo a077cb587a1b622e03aa4bf2f3689de14658a9497a9af2c427bba5f4cc3c4723 /usr/share/keyrings/getenvoy-keyring.gpg | sha256sum --check
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/getenvoy-keyring.gpg] https://deb.dl.getenvoy.io/public/deb/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/getenvoy.list
RUN apt-get update -y
RUN apt-get install -y getenvoy-envoy

## Directories

RUN mkdir /app
RUN mkdir /app/api
RUN mkdir /app/web
RUN mkdir /app/proxy
COPY ./api/ /app/api
COPY ./database/ /app/api
COPY ./models/ /app/api
COPY ./main.py /app/api
COPY ./requirements.txt /app/api
WORKDIR /app/api

## pip install

RUN pip3 install -r ./requirements.txt

## Volumes


## Nginx Config

## Envoy Config

## Ports

EXPOSE 80
EXPOSE 443
EXPOSE 50051
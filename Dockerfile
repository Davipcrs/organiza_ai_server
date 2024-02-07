FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive
ENV DATABASE_HOST=localhost
ENV DATABASE_PORT=5432
ENV DATABASE_USER=postgres
ENV DATABASE_PWD=postgres

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
RUN mkdir /app/server
RUN mkdir /app/server/api
RUN mkdir /app/server/database
RUN mkdir /app/server/models
RUN mkdir /app/web
RUN mkdir /app/proxy

## gRPC server copies

COPY ./api/ /app/server/api
COPY ./database/ /app/server/database
COPY ./models/ /app/server/models
COPY ./main.py /app/server
COPY ./__init__.py /app/server
COPY ./requirements.txt /app/server
COPY ./docker_entrypoint.sh /app/server

## pip install

WORKDIR /app/server
RUN pip3 install -r ./requirements.txt
RUN ls -la
## Volumes

## Flutter Web App Config

## Nginx Config

## Envoy Config

## Ports

EXPOSE 80
EXPOSE 443
EXPOSE 50051

RUN chmod +x /app/server/docker_entrypoint.sh
ENTRYPOINT [ "/app/server/docker_entrypoint.sh" ]
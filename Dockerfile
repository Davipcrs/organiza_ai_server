# Build flutter web.
FROM debian:latest as web-build-env
ARG DEBIAN_FRONTEND=noninteractive
# Copy the flutter app to the Nginx in port 80 or 443
# Add Envoy gRPC support

RUN apt-get upgrade -y
RUN apt-get update -y
RUN apt-get install git -y
RUN apt-get install curl git wget unzip libgconf-2-4 gdb libstdc++6 libglu1-mesa fonts-droid-fallback lib32stdc++6 python3 sed -y
RUN apt-get clean

RUN git clone https://github.com/flutter/flutter.git /usr/local/flutter

ENV PATH="${PATH}:/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin"

RUN flutter doctor -v
RUN flutter channel master
RUN flutter upgrade

RUN mkdir /app
RUN git clone https://github.com/Davipcrs/organiza_ai.git /app
WORKDIR /app
RUN flutter build web

FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive
ENV DATABASE_HOST=localhost
ENV DATABASE_PORT=5432
ENV DATABASE_USER=postgres
ENV DATABASE_PWD=postgres

RUN apt-get upgrade -y
RUN apt-get update -y
RUN apt-get install python3 python3-pip libpq-dev -y
# RUN apt-get install nginx -y
# pg_isready command
RUN apt-get install postgresql-client -y

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
## Volumes

## Nginx Config and Flutter Web App Config
#COPY ./default /etc/nginx/sites-enabled/default
#RUN nginx -V
#RUN cat /etc/nginx/sites-enabled/default
COPY --from=web-build-env /app/build/web /app/web
#RUN service nginx restart
#RUN service nginx reload

## Envoy Config

COPY ./envoy.yaml /app/proxy
WORKDIR /app/proxy

RUN envoy --version

## Ports

EXPOSE 80
EXPOSE 443
EXPOSE 9901
EXPOSE 50051
EXPOSE 50052

RUN apt-get clean

WORKDIR /app/server

RUN chmod +x /app/server/docker_entrypoint.sh
ENTRYPOINT [ "/app/server/docker_entrypoint.sh" ]
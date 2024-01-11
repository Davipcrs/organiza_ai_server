FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y
RUN mkdir /app
COPY . /app/
WORKDIR /app

RUN bash ./install_script.sh


## install nginx
## install MariaDB
# Variáveis de ambiente
## install Api
## install certbot-nginx
# Variáveis de ambiente
## install flutter-web

## Entrypoint docker_entrypoint.sh
# https://gist.github.com/nfsarmento/f193c98dfc255ef9bb059978a076dd65
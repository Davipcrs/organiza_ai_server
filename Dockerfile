FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 python3-pip
RUN apt-get -y install nginx postgresql 
RUN mkdir /app
COPY . /app/
WORKDIR /app

RUN pip3 install -r ./requirements.txt

# RUN bash ./install_script.sh

ARG DATABASE_USER=user
ARG DATABASE_PWD=password

ENV DATABASE_USER=$DATABASE_USER
ENV DATABASE_PWD=$DATABASE_PWD

USER postgres
RUN mkdir -p /var/lib/postgresql/data
RUN mkdir -p /run/postgresql
VOLUME /var/lib/postgresql/data
RUN chown -R postgres:postgres /var/lib/postgresql/data
RUN chown -R postgres:postgres /run/postgresql/
RUN chmod 0700 /run/postgresql/

RUN initdb -D /var/lib/postgresql/data

RUN createdb organiza_ai

ENTRYPOINT [ "sh", "./docker_entrypoint.sh" ]

## install nginx
## install MariaDB
# Variáveis de ambiente
## install Api
## install certbot-nginx
# Variáveis de ambiente
## install flutter-web

## Entrypoint docker_entrypoint.sh
# https://gist.github.com/nfsarmento/f193c98dfc255ef9bb059978a076dd65


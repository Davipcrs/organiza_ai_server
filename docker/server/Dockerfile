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

## pg_isready command
RUN apt-get install postgresql-client -y

RUN mkdir /app
RUN mkdir /app/server
RUN mkdir /app/server/api
RUN mkdir /app/server/database
RUN mkdir /app/server/models

COPY ./api/ /app/server/api
COPY ./database/ /app/server/database
COPY ./models/ /app/server/models
COPY ./main.py /app/server
COPY ./__init__.py /app/server
COPY ./requirements.txt /app/server
COPY ./server_docker_entrypoint.sh /app/server

WORKDIR /app/server
RUN pip3 install -r ./requirements.txt

EXPOSE 50052

RUN apt-get clean

WORKDIR /app/server

RUN chmod +x /app/server/server_docker_entrypoint.sh
ENTRYPOINT [ "/app/server/server_docker_entrypoint.sh" ]
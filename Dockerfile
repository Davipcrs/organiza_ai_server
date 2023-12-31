FROM ubuntu:24.04
RUN apt-get update && apt-get upgrade
RUN mkdir /app
WORKDIR /app

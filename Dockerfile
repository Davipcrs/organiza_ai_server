#FROM ubuntu:latest
#ARG DEBIAN_FRONTEND=noninteractive
#RUN apt-get update && apt-get upgrade -y
#RUN mkdir /app
#COPY . /app/
#WORKDIR /app

#RUN bash ./install_script.sh


## install nginx
## install MariaDB
# Variáveis de ambiente
## install Api
## install certbot-nginx
# Variáveis de ambiente
## install flutter-web

## Entrypoint docker_entrypoint.sh
# https://gist.github.com/nfsarmento/f193c98dfc255ef9bb059978a076dd65

# Use the Alpine Linux as the base image
FROM alpine:latest

# Install necessary packages
RUN apk update && \
    apk add --no-cache python3 py3-pip postgresql postgresql-dev gcc musl-dev

# Set environment variables for PostgreSQL
ENV DATABASE_USER=user
ENV DATABASE_PASSWORD=password
ENV POSTGRES_DB=organiza_ai

# Set up PostgreSQL
RUN mkdir -p /var/lib/postgresql/data
VOLUME /var/lib/postgresql/data
RUN initdb -D /var/lib/postgresql/data && \
    pg_ctl -D /var/lib/postgresql/data -l logfile start && \
    createdb $POSTGRES_DB && \
    psql -d $POSTGRES_DB -c "CREATE USER $POSTGRES_USER WITH ENCRYPTED PASSWORD '$POSTGRES_PASSWORD';" && \
    psql -d $POSTGRES_DB -c "GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;"


# Copy gRPC server code into the container
RUN mkdir -p /server/grpc


# Set the working directory
WORKDIR /server/grpc

COPY . .
RUN pip3 install -r ./requirements.txt


# Expose the gRPC port
EXPOSE 5432
EXPOSE 50051

# Command to start services
CMD ["sh", "-c", "pg_ctl -D /var/lib/postgresql/data -l logfile start && python3 /server/grpc/main.py"]
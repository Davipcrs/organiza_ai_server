FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y
RUN apt-get install postgresql-14 postgresql-contrib-14 libpq-dev -y
# python3 python3-pip nginx
# psycopg2 req: libpq-dev

EXPOSE 5432

# RUN pip3 install -r ./requirements.txt

# RUN bash ./install_script.sh

ARG DATABASE_USER=user
ARG DATABASE_PWD=password

ENV DATABASE_USER=$DATABASE_USER
ENV DATABASE_PWD=$DATABASE_PWD
ENV PATH=$PATH:/usr/lib/postgresql/14/bin

USER root
RUN service postgresql start

RUN mkdir /app
RUN mkdir -p /var/lib/postgresql/data
RUN mkdir -p /run/postgresql
RUN mkdir -p /var/run/postgresql
# RUN ln -s /tmp/.s.PGSQL.5432 /var/run/postgresql/.s.PGSQL.5432 
VOLUME /var/lib/postgresql/data
# Permissions
RUN chown -R postgres:postgres /var/lib/postgresql/data
RUN chown -R postgres:postgres /run/postgresql/
RUN chown -R postgres:postgres /var/run/postgresql
RUN chown -R postgres:postgres /var/lib/postgresql/14/main
RUN chown postgres:postgres /run/postgresql/.s.PGSQL.5432
# RUN chown postgres:postgres /var/lib/postgresql/14/main/pg_hba.conf
RUN chmod 700 -R /run/postgresql/
RUN chmod 700 -R /var/lib/postgresql/14/main
RUN chmod 777 /var/run/postgresql/.s.PGSQL.5432
# RUN chmod 700 /var/lib/postgresql/14/main/pg_hba.conf

COPY . /app/
WORKDIR /app

USER postgres
RUN initdb -D /var/lib/postgresql/data

USER root


RUN sed -i "s|listen_addresses = 'localhost'|listen_addresses = '*' |g" /var/lib/postgresql/data/postgresql.conf
RUN sed -ie '/port = /s/.*/port = 5432/' /var/lib/postgresql/data/postgresql.conf
# RUN echo host    all  all  0.0.0.0/0  md5 > /var/lib/postgresql/data/pg_hba.conf
# RUN echo local   all             postgres                                md5 >/var/lib/postgresql/data/pg_hba.conf
RUN service postgresql restart




# RUN echo port=5432 > /etc/postgresql/14/main/postgresql.conf


# RUN service postgresql restart


USER postgres
# RUN /usr/lib/postgresql/14/bin/pg_ctl restart -D /var/lib/postgresql/14/main
RUN ls -la /var/run/postgresql/
RUN ls -la /var/lib/postgresql/data
RUN cat /var/lib/postgresql/data/postgresql.conf | grep port
RUN cat /var/lib/postgresql/data/pg_hba.conf
RUN createdb organiza_ai
# RUN psql CREATE DATABASE organiza_ai;

USER root

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


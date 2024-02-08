#!/bin/sh

check_pg_ready(){
    pg_isready -d organiza_ai -h $DATABASE_HOST -p $DATABASE_PORT -U $DATABASE_USER
}
if check_pg_ready; then

    python3 /app/server/main.py & 
    envoy -c /app/proxy/envoy.yaml
    exit 0
fi

bash /app/server/docker_entrypoint.sh
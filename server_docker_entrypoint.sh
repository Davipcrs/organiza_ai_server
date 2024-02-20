#!/bin/sh

check_pg_ready(){
    pg_isready -d organiza_ai -h $DATABASE_HOST -p $DATABASE_PORT -U $DATABASE_USER
}
sleep 5
if check_pg_ready; then
    python3 /app/server/main.py

fi
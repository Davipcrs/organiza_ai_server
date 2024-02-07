#!/bin/sh
python3 /app/server/main.py & 
envoy -c /app/proxy/envoy.yaml
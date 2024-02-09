#!/bin/sh

#echo "Configure internal /etc/hosts for organiza_ai.com dns name"

echo "building image..."
sudo docker build . -t grpc-organiza_ai --no-cache --progress=plain

echo "Image builded..."
echo \n
echo "Running docker compose"
sudo docker compose up -d


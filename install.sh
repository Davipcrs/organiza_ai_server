#!/bin/sh


web_install(){
    mv $PWD/docker/web/Dockerfile ./Dockerfile
    echo "building image..."
    sudo docker build -f $PWD/Dockerfile -t grpc-organiza_ai --no-cache --progress=plain .
    echo "Image builded..."
    echo \n
    echo "Running docker compose"
    sudo docker compose up -d
    exit 0
}

headless_install(){
    mv $PWD/docker/server/Dockerfile ./Dockerfile
    echo "building image..."
    sudo docker build -f $PWD/Dockerfile -t grpc-organiza_ai --no-cache --progress=plain .
    echo "Image builded..."
    echo \n
    echo "Running docker compose"
    sudo docker compose up -d
    exit 0
}


#echo "Configure internal /etc/hosts for organiza_ai.com dns name"

echo "Thanks for deploying Organiza_ai server in your linux system!"
echo \n
echo "Check the docker-compose.yaml file in the directory $PWD"
echo \n
cat $PWD/docker-compose.yaml
echo \n
read -p "The host settings are correct? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
echo \n
echo "Installing the server!"
read -p "You want to install the gRPC Web Support? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || headless_install
web_install





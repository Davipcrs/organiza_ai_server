#!/bin/sh


web_install(){
    echo "building image..."
    sudo docker build web.Dockerfile -t grpc-organiza_ai --no-cache --progress=plain

    echo "Image builded..."
    echo \n
    echo "Running docker compose"
    sudo docker compose up -d
    exit 0
}

headless_install(){
    echo "building image..."
    sudo docker build server.Dockerfile -t grpc-organiza_ai --no-cache --progress=plain

    echo "Image builded..."
    echo \n
    echo "Running docker compose"
    sudo docker compose up -d
    exit 0
}


#echo "Configure internal /etc/hosts for organiza_ai.com dns name"

echo "Thanks for deploying Organiza_ai server in your linux system!"
echo \n
echo "Installing the server!"
read -p "You want to install the gRPC Web Support? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || headless_install();
web_install();






# Organiza aí Backend Server

## This Repository Holds the code for the Python gRPC server

Note: This gRPC server needs a Proxy for gRPC-Web (Check the gRPC docs)  
  
This backend server is responsible to create the Tables for the database, quering the database and returning the values to the application via
gRPC protocol.  
In the /database folder you can see the code for the quering.  
In /models folders is the Table definition.  
In the /api is the gRPC code, the .proto file and auto-generated files from the "protoc".  
Is recomended to use venv to run locally this code.  

## Deploying

(For using the UI check the UI Repo: <https://github.com/Davipcrs/organiza_ai/>)  

Clone this repo  

```bash
git clone https://github.com/Davipcrs/organiza_ai_server.git  
```

Change the directory and give permissions  

```bash
cd organiza_ai_server  
sudo chmod +x ./install.sh  
```

**CAUTION!**

The server IP needs to be changed in the docker-compose.yaml before running the ./install.sh  

```bash
./install.sh  
```

Open ports for the server to Work!  

```bash
# in ubuntu:
sudo ufw allow 80, 443, 50051, 50052

# in RHEL based linux (Firewalld):
sudo firewall-cmd --permanent --add-port={80/tcp,443/tcp,50051/tcp,50052/tcp}
sudo firewall-cmd --reload

# You can override the ports on the docker compose and then override here.
# If your linux distro do not use these firewalls service look into how open that ports.
```

## (Bugs that i was trying to resolve)  

For deploying this application in Web is necessary:  
    - disable the system firewall as flutter tends to connect to random ports for the gRPC.  
    - need to point a DNS name "organiza_ai.com" to the server IP.  

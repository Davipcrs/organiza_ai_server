# Organiza aí Backend Server

## This Repository Holds the code for the Python gRPC server

Note: This gRPC server needs a Proxy for gRPC-Web (Check the gRPC docs)  
  
This backend server is responsible to create the Tables for the database, quering the database and returning the values to the application via
gRPC protocol. In the /database folder you can see the code for the quering. In /models folders is the Table definition. In the /api is the gRPC
code, the .proto file and auto-generated files from the "protoc". Is recomended to use venv to run locally this code.  

## Deploying

clone this repo: git clone <https://github.com/Davipcrs/organiza_ai_server.git>
run: cd organiza_ai_server  
run: sudo chmod +x ./install.sh  
run: ./install.sh  

(Bugs that i was trying to resolve)  
For deploying this application is necessary:  
    - disable the system firewall as flutter tends to connect to random ports for the gRPC.  
    - the server IP needs to be changed in the docker-compose.yaml before running the ./install.sh  
    - for the web-ui works need to point a DNS name "organiza_ai.com" to the server IP.  

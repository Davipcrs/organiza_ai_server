# Organiza aí Backend Server

## This Repository Holds the code for the Python gRPC server

Note: This gRPC server needs a Proxy for gRPC-Web (Check the gRPC docs)  
  
This backend server is responsible to create the Tables for the database, quering the database and returning the values to the application via
gRPC protocol. In the /database folder you can see the code for the quering. In /models folders is the Table definition. In the /api is the gRPC
code, the .proto file and auto-generated files from the "protoc". Is recomended to use venv to run locally this code.  

Look at the docker-compose.yaml file for deploying the server.

# OttoBotServer
OttoBot: Voice interface based conversation bot in the domain of equity investment.

## Description
OttoBotServer is the backbone of OttoBot chatbot. This Flask application runs in a Docker container on a AWS EC2 instance (component 3) receives requests from Lambda function (component 2).  
The request is parsed for intents and other data, suitable response is generated and handed back to Lambda function.

## Components
user input (Alexa) —> Lambda —> EC2 —> Docker inside EC2 instance (flask server)

1. Alexa

    Description: Handle incoming user requests from Alexa app, parse intents from raw data.  
    Builds from raw data structured json request with intents and slots.  
	Passes the structured json to lambda.
<br><br>
2. Lambda

	Name: OttoBotLambda  
	Region: EU (Ireland)  
	VPC: OttoBotVPC  
	SecurityGroup: OttoBotLambdaSG  
	subnet: eu-west-1a 10.0.1.0 - eu-west-1a (public)  
	Role: sending requests to private IP of EC2 instance  
	Description:
		Routes requests from ASK APIs to the backend server (EC2 instance called OttoBotServer) to generate response. OttoBotLambda is a middle-man, forwards structured json request from Alexa to EC2 via network POST request.
<br><br>
3. EC2

	Name: OttoBotServer  
	Region: EU (Ireland)  
	Availability zone: eu-central-1b  
	Private IP address: 10.0.2.152  
	Role: receiving requests on port 80 (http://10.0.2.152/api/) and forwarding requests to port 3333 (Docker listening there)  
	Description:
		Server running Docker for handling incoming requests on address http://10.0.2.152/api/. Passes requests coming on port 80 to port 3333 where Docker is listening.
<br><br>
4. Docker

	Name: drabekj/ottobot  
	receiving requests on port 3333  
	Description:  
		Handles all the logic, acts upon the incoming request, generates response (structured json file) and answers the POST request with the build response.

## Setup docker
Run the refresh_docker.sh script or execute the followind steps.  

1) Stop any running docker instances (optional)

	`sudo docker stop $(docker ps -aq)`

2) Download OttoBot latest docker container:

	`docker pull drabekj/ottobot`

3) Run Docker container (second port '3333' is the one EXPOSEd in Dockerfile), forwarding hosts port 80 to docker to port 3333:

	`docker run -p 80:3333 drabekj/ottobot`

## Publish new version
Run the docker_publish.sh script or execute the followind steps.  

1) Build new docker image from the project folder and set the environment variable DATABASE_URL to database url including login

	`sudo docker build ~/ProjectFolder/ --build-arg DB=$(echo $DATABASE_URL)` -t ottobot

2) Rename the created image

	`docker tag ottobot drabekj/ottobot`

3) Publish the new docker image to the Docker Hub

	`docker push drabekj/ottobot`

# OttoBotServer
OttoBot: Voice interface based conversation bot in the domain of equity investment.

## Description
OttoBotServer is the backbone of OttoBot chatbot. This Flask application runs in a Docker container on a AWS EC2 instance (component 3) receives requests from Lambda function (component 2).
The request is parsed for intents and other data, suitable response is generated and handed back to Lambda function.

## Components
:speech_balloon: user input (Alexa) —> Lambda —> EC2 —> Docker inside EC2 (flask server)

1. Alexa

    Description: Handle incoming user requests from Alexa app, parse intents from raw data.  
    Builds from raw data structured json request with intents and slots.
Passes the structured json to lambda.

2. Lambda

	Name: OttoBotLambda
	Region: EU (Ireland)  
	Role: sending requests to public IP of EC2 instance 

	Description:
		Forwards structured json request from Alexa to EC2 via network POST.

3. EC2

	Name: OttoBotServer  
	Region: EU (Frankfurt)  
	Availability zone: eu-central-1b
	Public IP address (elastic IP): 52.58.219.129
	Role: receiving requests on port 80 and forwarding requests to port 3333 (Docker listening there)

	Description:
		Server running Docker for handling incoming requests. Passes requests coming on port 80 to port 3333 where Docker is listening.

4. Docker

	Name: drabekj/ottobot  
	receiving requests on port 3333

	Description:
		Handles all the logic, acts upon the incoming request, generates response (structured json file) and answers the POST request with the build response.

## Setup docker :wrench:
1) Stop any running docker instances (optional)

	`sudo docker stop `docker ps -aq``

2) Download OttoBot latest docker container:

        `docker pull drabekj/ottobot`

3) Run Docker container (second port '3333' is the one EXPOSEd in Dockerfile), forwarding hosts port 80 to docker to ort 3333:

        `docker run -p 80:3333 drabekj/ottobot`

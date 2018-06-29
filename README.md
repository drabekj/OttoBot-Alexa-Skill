# OttoBot Alexa skill
<p align="center">
<img src="https://github.com/drabekj/OttoBotServer/blob/master/documentation/img/logo.png" width="250">
</p>
OttoBot is a skill for Amazon Alexa which helps it's users with stock market investing. It aims at beginners and general public interested in getting into the investing domain, delivering easy to use experience thanks tho the voice user interface.
The application backend runs on the AWS cloud platform.

# Table of Contents
1. [Skill demo](#skill-demo)  
    1.1 [Interaction demonstration](#interaction-demonstration)  
2. [Technical overview](#technical-overview)
3. [Component 1: Interaction model](#component-1-interaction-model)
4. [Component 2: Backend server](#component-2-backend-server)  
    4.1 [Infrastructure](#infrastructure)  
    4.1.1 [Detailed components description](#detailed-components-description)  
    4.2 [Flask server](#flask-server)  
    4.3 [Flask server code structure](#flask-server-code-structure)  
    4.4 [Utilities](#utilities)


## Skill demo
OttoBot is a stock market trading helper. The Skill provides information about current stock market status, news, offers virtual portfolios, and is even capable of explaining some of the advanced trading terminologies.
All of this will help you learn about the trading market and provide infor- mation to make better investing decisions.

**To Enable the Skill:** Search for “OttoBot” in the Alexa mobile app or at Amazon.com. Once you find the skill, open the detail and click the enable button.

**To Get Started:** Say *”Alexa open Otto investments”*.

**Interaction Examples:**
  - *“What is the value of Apple stock?”*
  - *“Add Microsoft to my portfolio.”*
  - *“How is my portfolio doing?”*
  - *“Give me the latest news on Tesla.”*
  - *“What is P/E ratio?”*

### Interaction demonstration:
<p align="center">
<img src="https://github.com/drabekj/OttoBotServer/blob/master/documentation/img/dialog.png" width="600">
</p>

## Technical overview
The application itself resides in the cloud and has 2 main components:
1. Alexa interaction model (ASK API) - responsible for NLU and requests matching and parsing
2. The backend server component - responsible for generating appropriate responses

<p align="center">
<img src="https://github.com/drabekj/OttoBotServer/blob/master/documentation/img/alexa_components.png" width="600">
</p>

User's request made on a Alexa-enabled device is sent in a raw form to the Alexa cloud where it is parsed and matched to the defined interaction model. After that, a JSON file is send to the backend server which is responsible for generating an appripriate response. As soon as the JSON response is generated, it is passed back to the device and presented to the user.


## Component 1: Interaction model
In the interaction model, there are defined the different intents and sample utterances for each intent, as well as variables (so called Slots).
The interaction model is defined through the web interface on https://developer.amazon.com/edw/home.html, however, it can be exported/imported to a JSON configuration file.  
The interaction model for OttoBot is in *interaction_model.json*.

<p align="center">
<img src="https://github.com/drabekj/OttoBotServer/blob/master/documentation/img/int_model_stock_price.png" width="400">
</p>

## Component 2: Backend server
The backend server is responsible for generating responses based on the incomming JSON file.


### Infrastructure
As stated earlier, the request travels from the Alexa-enabled device, to the ASK API in the cloud (for which a interaction model is defined). After that the request is sent to a AWS Lambda function for the purpose of decoupling, the OttoBotLambda function forwards it than to a AWS EC2 instance where a Flask server is responsible for generating a response.
Additionally, a database is used to store users data (like stock portfolio), and allow synchronisation across multiple devices based on Facebook authentication API.  
The whole infrastructure is inside a AWS VPC (virtual private cloud), with strict security groups and port blocking rules to ensure security.  
Simply put, there are 2 subnets, a **public 10.0.1.0** and a **private 10.0.2.0**. The Flask server resides inside the private subnet and can be only accessed through the public subnet, **not** from the outside world, for this purpose, a EC2 debug server exists. A Lambda function receives the requests from ASK API and forwards the requests to the Flask server.
The infrastructure is shown on the image below.

<p align="center">
<img src="https://github.com/drabekj/OttoBotServer/blob/master/documentation/img/infractracture_diagram.png" width="800">
</p>

#### Detailed components description
1. Lambda

	Name: OttoBotLambda  
	Region: EU (Ireland)  
	VPC: OttoBotVPC  
	SecurityGroup: OttoBotLambdaSG  
	subnet: eu-west-1a 10.0.1.0 - eu-west-1a (public)  
	Role: sending requests to private IP of EC2 instance  
	Description:
		Routes requests from ASK APIs to the backend server (EC2 instance called OttoBotServer) to generate response. OttoBotLambda is a middle-man, forwards structured json request from Alexa to EC2 via network POST request.
<br><br>
2. EC2

	Name: OttoBotServer  
	Region: EU (Ireland)  
	Availability zone: eu-central-1b  
	Private IP address: 10.0.2.152  
	Role: receiving requests on port 80 (http://10.0.2.152/api/) and forwarding requests to port 3333 (Docker listening there)  
	Description:
		Server running Docker for handling incoming requests on address http://10.0.2.152/api/. Passes requests coming on port 80 to port 3333 where Docker is listening.
<br><br>
3. Docker

	Name: drabekj/ottobot  
	receiving requests on port 3333  
	Description:  
		Handles all the logic, acts upon the incoming request, generates response (structured json file) and answers the POST request with the build response.

### Flask server
The backend is a AWS EC2 instance running a Flask server inside a Docker container.

<p align="center">
<img src="https://github.com/drabekj/OttoBotServer/blob/master/documentation/img/dockerized_app.png" width="250">
</p>

The backend Flask server exposes it's API at http://10.0.2.152/api/ to the local network, where it expects a POST request with the parsed JSON request.

#### Flask server code structure
There are 3 types of requests to be expected:
- LaunchRequest - occures when user opens the app by invocation name (`Otto Investments`)
- EndRequest - occures when user says something like *"Alexa STOP"*
- IntentRequest - most common type, represents a intention of the user to do something.

Based on the type of the request, specific module of the Flask server handles the response generation. In case of the IntentRequest, it is further delegated based on the future the user is targeting (e.g. StockPrice). This flow is shown on the diagram below.

<p align="center">
<img src="https://github.com/drabekj/OttoBotServer/blob/master/documentation/img/request_delegation.png" width="600">
</p>

#### Utilities
The easily work with the Docker images, I created 2 scripts.
1. The ***docker_publish.sh*** script - is for publishing new version of the application. It creates new version based on the source code in the directory and publishes it to the DockerHub.  (!!! database URL needs to be included in the local shell variable $DATABASE_URL)
2. The ***refresh_docker.sh*** script - is for updating the running Docker container on the EC2 server (needs to be executed on the server). It stops the current container, pulls the new version and runs it.



#!/bin/bash
sudo docker stop `docker ps -aq` &&
sudo docker pull drabekj/ottobot &&
sudo docker run -p 80:3333 drabekj/ottobot

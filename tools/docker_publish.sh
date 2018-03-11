#!/bin/bash

docker build ~/Documents/Developer/Python/Alexa/OttoBot/OttoBotServer/ --build-arg DB=`echo $DATABASE_URL` -t ottobot
docker tag ottobot drabekj/ottobot
docker push drabekj/ottobot

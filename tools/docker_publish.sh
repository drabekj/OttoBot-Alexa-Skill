#!/bin/bash

docker build ../ -t ottobot
docker tag ottobot drabekj/ottobot
docker push drabekj/ottobot

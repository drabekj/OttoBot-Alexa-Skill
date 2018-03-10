FROM ubuntu:16.04
MAINTAINER Jan Drabek <drabek.honza@gmail.com>

ENV APP_CONTAINER_PATH="/code"

# Update system and install basic tools
RUN apt-get update -y && \
    apt-get install -y python3-pip

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir ${APP_CONTAINER_PATH}/
WORKDIR ${APP_CONTAINER_PATH}/
COPY . ${APP_CONTAINER_PATH}/

# Pip install any needed packages specified in requirements.txt
RUN pip3 install -r ${APP_CONTAINER_PATH}/requirements.txt

EXPOSE 3333

# Application configuration
ENV APP_SETTINGS="production"

CMD python3 run.py
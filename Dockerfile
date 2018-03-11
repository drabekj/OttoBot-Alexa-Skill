FROM python:alpine
MAINTAINER Jan Drabek <drabek.honza@gmail.com>

ENV APP_CONTAINER_PATH="/code"

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir ${APP_CONTAINER_PATH}/
WORKDIR ${APP_CONTAINER_PATH}/
COPY . ${APP_CONTAINER_PATH}/

# Update system and install basic tools and requirements (afterwards remove no longer necessary dependencies)
RUN apk update && \
 apk add python3 python3-dev mariadb-dev build-base  && \
 apk add --virtual .build-deps gcc python3-dev musl-dev && \
 python3 -m pip install -r ${APP_CONTAINER_PATH}/requirements.txt --no-cache-dir && \
 apk del python3-dev mariadb-dev build-base && \
 apk --purge del .build-deps && \
 apk add mariadb-client-libs

EXPOSE 3333

# Application configuration
ENV APP_SETTINGS="production"

# Argument from command line when building Docker image (--build-arg)
ARG DB="mysql://user:password@host/db_name"
ENV DATABASE_URL=${DB}

CMD python3 run.py
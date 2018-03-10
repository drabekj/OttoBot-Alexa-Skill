FROM python:alpine
MAINTAINER Jan Drabek <drabek.honza@gmail.com>

ENV APP_CONTAINER_PATH="/code"

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir ${APP_CONTAINER_PATH}/
WORKDIR ${APP_CONTAINER_PATH}/
COPY . ${APP_CONTAINER_PATH}/

# Update system and install basic tools and requirements (afterwards remove no longer necessary dependencies)
RUN apk update && \
 apk add python3 postgresql-libs && \
 apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r ${APP_CONTAINER_PATH}/requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

EXPOSE 3333

# Application configuration
ENV APP_SETTINGS="production"
ENV DATABASE_URL="mysql://username:password@host/db_name"

CMD python3 run.py
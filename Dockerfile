# syntax=docker/dockerfile:1
FROM python:2
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y libmemcached-dev
WORKDIR /code
COPY . /code/
VOLUME /code
RUN pip install -r requirements.txt
RUN chmod +x ./run.sh
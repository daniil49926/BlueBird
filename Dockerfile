FROM python:3.10.5-slim

WORKDIR /blue_bird
COPY . /blue_bird

RUN pip install -r requirements.txt
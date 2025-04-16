FROM python:3.12-slim-bullseye

RUN pip install --no-cache-dir elasticsearch==8.18.0 certifi

COPY . /opt/elasticsearch-manage

WORKDIR /opt/elasticsearch-manage

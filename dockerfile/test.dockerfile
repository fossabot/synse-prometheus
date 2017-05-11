FROM python:3.6-alpine
MAINTAINER Klemente Gilbert-Espada <klemente@vapor.io>

ADD . /synse-prometheus
WORKDIR /synse-prometheus

RUN mkdir /logs
RUN apk add --update alpine-sdk python3-dev && \
  pip install -r /synse-prometheus/testing-requirements.txt && \
  pip install -r /synse-prometheus/requirements.txt

WORKDIR /synse-prometheus
CMD /bin/sh -c "while true; do sleep 100; done"

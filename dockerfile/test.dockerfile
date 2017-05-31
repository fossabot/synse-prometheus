FROM python:3.6-alpine
MAINTAINER Klemente Gilbert-Espada <klemente@vapor.io>

RUN mkdir /logs
RUN apk add --update alpine-sdk python3-dev
# A copy of the whole directory causes package rebuilds every time. This
# limits rebuilds to only package changes.
COPY requirements.txt /synse-prometheus/requirements.txt
COPY testing-requirements.txt /synse-prometheus/testing-requirements.txt

RUN pip install -r /synse-prometheus/testing-requirements.txt && \
  pip install -r /synse-prometheus/requirements.txt

WORKDIR /synse-prometheus
CMD /bin/sh -c "while true; do sleep 100; done"

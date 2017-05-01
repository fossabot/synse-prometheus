FROM python:3.6-alpine
MAINTAINER Klemente Gilbert-Espada <klemente@vapor.io>

ADD ./prometheus/requirements.txt requirements.txt

# Install dependencies
RUN set -e; \
  pip3 install -r requirements.txt ;

RUN mkdir /logs

ADD . /synse-prometheus
WORKDIR /synse-prometheus

# Expose our API endpoint port.
EXPOSE 9243

# Define default command
CMD ["./start_synse_prometheus.sh"]
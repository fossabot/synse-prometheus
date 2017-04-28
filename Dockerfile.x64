FROM python:3.6-alpine
MAINTAINER Klemente Gilbert-Espada <klemente@vapor.io>

ADD ./prometheus/requirements.txt requirements.txt

# Install dependencies
RUN set -e; \
  apk update && \
  apk add nginx openrc --no-cache ; \
  adduser -D -u 1000 -G www-data www-data && \
  apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    linux-headers \
  ; \
  pip3 install -r requirements.txt ; \
  apk del .build-deps

RUN mkdir -p /etc/uwsgi && \
    touch /etc/uwsgi/reload && \
    chown -R www-data:www-data /etc/uwsgi && \
    mkdir /run/nginx && \
    chown -R www-data:www-data /var/lib/nginx && \
    chown -R www-data:www-data /run/nginx && \
    mkdir /logs && \
    chown root:www-data /logs && \
    chmod 775 /logs

ADD . /synse-prometheus
WORKDIR /synse-prometheus

# run command for nginx configuration
RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.orig ; \
    cp /synse-prometheus/prometheus_nginx.conf /etc/nginx/nginx.conf

# Expose our API endpoint port.
EXPOSE 9243

# Define default command
CMD ["./start_synse_prometheus.sh"]
#!/bin/sh

chown root:www-data /logs
chmod 775 /logs

nginx &

uwsgi /synse-prometheus/prometheus_uwsgi.ini 2>&1
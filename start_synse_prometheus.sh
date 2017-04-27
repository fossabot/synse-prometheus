#!/bin/bash

chown root:www-data /logs
chmod 775 /logs

service nginx restart 2>&1

uwsgi /synse-prometheus/prometheus_uwsgi.ini 2>&1
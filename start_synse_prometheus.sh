#!/bin/sh

chown root:www-data /logs
chmod 775 /logs

python /synse-prometheus/prometheus/runserver.py
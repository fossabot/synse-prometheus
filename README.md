# Synse-prometheus

Synse-prometheus provides a standalone docker container/flask app for collecting data from Synse through a Prometheus client, and making that data available to Prometheus servers that would consume it.

## Running and using synse-prometheus
* To specify which synse-server instance to collect data from, set the SYNSE_SERVER environment variable to the url of the server.
* Use the command `make run` from inside the primary directory of the repo to launch the container. It should start collecting data from synse-server shortly afterwards.
* To access the data that synse-prometheus is collecting, send a request to the http://[synse-prometheus' local ip]:9243/prometheus/metrics endpoint. This is the mechanism through which prometheus servers can retrieve the collected data.

The synse-prometheus container also has a /prometheus/test endpoint which is used for verifying that the container is working correctly.
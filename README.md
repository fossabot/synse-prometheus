# Synse-prometheus

Synse-prometheus provides a standalone docker container/flask app for collecting data from Synse through a Prometheus client, and making that data available to Prometheus servers that would consume it.

## Running and using synse-prometheus
* To specify which synse-server instance to collect data from, set the SYNSE_SERVER environment variable to the url of the server.
* Use the command `make run` from inside the primary directory of the repo to launch the container. It should start collecting data from synse-server shortly afterwards. The default interval is 5 minutes.
* To access the data that synse-prometheus is collecting, send a request to the http://[synse-prometheus' local ip]:9243/metrics endpoint. This is the mechanism through which prometheus servers can retrieve the collected data.

The synse-prometheus container also has a /test endpoint which is used for verifying that the container is working correctly.

## Running a Prometheus server
Here is a sample configuration file for a Prometheus server that can be run on localhost, or in a Docker container. Complete documentation can be found here: https://prometheus.io/docs/introduction/install/

To run a Prometheus Docker container, create a local configuration file ```prometheus.yml``` using the snippet below as a template.
Update the ```- targets``` field to point to the synse-prometheus container.
```
global:
  scrape_interval:     15s

scrape_configs:
  - job_name: 'synse'

    # Override the global default
    scrape_interval: 300s

    static_configs:
      - targets: ['192.168.99.100:9243']
```
Then use the Docker command below to mount the config file and start the container.
```
docker run -p 9090:9090 -v <local_config_directory>/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```

Prometheus is visible at localhost:9090

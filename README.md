synse-promethus is a prometheus exporter for synse-server's metrics. This enables you to ingest all your metrics into prometheus and use it for alerting/monitoring.

# Kick the tires

```bash
make run
```

To keep everything tied together, this starts a prometheus server up for you. Send your browser to `http://localhost:9090` and play around.

To stop it, you can run:

```bash
make down
```

Note: the default configuration uses the embedded synse-server and ipmi emulator. If you'd like to use a different backend, check out `--help`.

# Usage

```bash
docker run -it --rm vaporio/synse-prometheus python runserver.py --help
```

- To specify which synse-graphql instance to collect data from, set the SYNSE_GRAPHQL environment variable to the url of the graphql server.
- Configure your prometheus server. For more detailed documentation, see the [prometheus docs]. An example config:

```yaml
global:
  scrape_interval:     15s

scrape_configs:
  - job_name: 'synse'

    # Override the global default
    scrape_interval: 300s

    static_configs:
      - targets: ['synse-prometheus:9243']
```

# Development

## Run the server

```bash
make build dev
python runserver.py
```

- From outside the container (or inside it), you can run `curl localhost:9243`

## Run the tests (as part of development)

```
make build dev
tox
```

See [nosetests](http://nose.readthedocs.io/en/latest/usage.html) for some more examples. Adding `@attr('now')` to the top of a function is a really convenient way to just run a single test.

[prometheus-docs]: https://prometheus.io/docs/introduction/install/

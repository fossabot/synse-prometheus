# !! DEPRECATED !!
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fvapor-ware%2Fsynse-prometheus.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fvapor-ware%2Fsynse-prometheus?ref=badge_shield)

This repository is deprecated. Official support for the Prometheus exporter for Synse Server now lives in the [Synse GraphQL](https://github.com/vapor-ware/synse-graphql) repository.

-------------------------


synse-prometheus provides a [Prometheus][prometheus] exporter for the metrics being provided by your data center and IT equipment. You can use this, in conjunction with Prometheus to monitor these metrics and alert on them.

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
[prometheus]: https://prometheus.io/


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fvapor-ware%2Fsynse-prometheus.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fvapor-ware%2Fsynse-prometheus?ref=badge_large)
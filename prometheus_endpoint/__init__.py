#!/usr/bin/env python
""" Prometheus Endpoint

    Author:  Klemente Gilbert-Espada
    Date:    2/27/2017

    \\//
     \/apor IO
"""

import json
import logging.config
import os

from flask import Flask, jsonify

import prometheus_endpoint.config
import prometheus_endpoint.prometheus
from prometheus_client import Counter


def setup_logging(name="logging.json"):
    path = os.path.join(os.path.dirname(__file__), "..", name)
    with open(path, 'rt') as f:
        _config = json.load(f)
    logging.config.dictConfig(_config)

app = Flask(__name__)
test_counter = Counter('test_counter', 'number of times the test endpoint has been reached')


@app.route('/test', methods=['GET', 'POST'])
def test_routine():
    """ Test routine to verify the endpoint is running and ok
    without relying on other dependencies.
    """
    # We increment the test counter here as a means of updating the metrics
    # in some arbitrary way so that calls to the /metrics endpoint should
    # return new results if there's a call to the /test endpoint between them
    test_counter.inc()
    return jsonify({'status': 'ok'})

app.add_url_rule(
    '/metrics',
    view_func=prometheus_endpoint.prometheus.metrics
)


def main():
    prometheus_endpoint.prometheus.refresh()
    app.run(host='0.0.0.0', port=prometheus_endpoint.config.options.get('port'))


if __name__ == '__main__':
    main()

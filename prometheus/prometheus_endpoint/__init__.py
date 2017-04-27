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

def setup_logging(name="logging.json"):
    path = os.path.join(os.path.dirname(__file__), "..", name)
    with open(path, 'rt') as f:
        config = json.load(f)
    logging.config.dictConfig(config)


app = Flask(__name__)


@app.route('/prometheus/test', methods=['GET', 'POST'])
def test_routine():
    """ Test routine to verify the endpoint is running and ok
    without relying on other dependencies.
    """
    return jsonify({'status': 'ok'})

app.add_url_rule(
    '/prometheus/metrics',
    view_func=prometheus_endpoint.prometheus.metrics
)


def main():
    prometheus_endpoint.prometheus.refresh()
    app.run(host='0.0.0.0', port=prometheus_endpoint.config.options.get('port'))


if __name__ == '__main__':
    main()

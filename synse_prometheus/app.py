import json
import logging.config
import os

from flask import Flask, jsonify
from prometheus_client import Counter

from . import config, prometheus


def setup_logging(name="logging.json"):
    path = os.path.join(os.path.dirname(__file__), "..", name)
    with open(path, 'rt') as f:
        _config = json.load(f)
    logging.config.dictConfig(_config)


app = Flask(__name__)
app.add_url_rule(
    '/metrics',
    view_func=prometheus.metrics)

test_counter = Counter(
    'test_counter', 'number of times the test endpoint has been reached')


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


def main():
    prometheus.refresh()
    app.run(host='0.0.0.0', port=config.options.get('port'))


if __name__ == '__main__':
    main()

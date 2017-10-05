""" Tests for the synse-prometheus endpoints

    Author: Klemente Gilbert-Espada
    Date:   5/10/2017

    \\//
     \/apor IO

-------------------------------
Copyright (C) 2015-17  Vapor IO
"""

import json

import testtools
from requests import get

import synse_prometheus.app


class TestEndpoints(testtools.TestCase):

    def setUp(self):
        super(TestEndpoints, self).setUp()
        synse_prometheus.app.app.testing = True
        self.app = synse_prometheus.app.app.test_client()

    def request(self, url):
        """ Helper function for making get requests.
        :param url: the URL to make the request to
        :returns the request response
        """
        r = get(url)
        self.assertEqual(r.status_code, 200)
        return r

    def test_test_endpoint(self):
        """ Hit the /test endpoint and confirm that it returns
        the correct response.
        """
        response = self.app.get('/test')
        self.assertEqual(
            json.loads(response.get_data(True)).get('status'), 'ok')

    def test_metrics_endpoint(self):
        """ Hit the /metrics endpoint twice, confirming that it returns
        different results after more data has been collected.
        """
        first_response = self.app.get('/metrics')

        # Hit the test endpoint in order to
        # update the results from the metrics endpoint
        self.app.get('/test')

        second_response = self.app.get('/metrics')
        self.assertNotEqual(
            first_response.get_data(True), second_response.get_data(True))

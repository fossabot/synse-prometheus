""" Tests for the synse-prometheus endpoints

    Author: Klemente Gilbert-Espada
    Date:   5/10/2017

    \\//
     \/apor IO

-------------------------------
Copyright (C) 2015-17  Vapor IO

This file is part of Synse.

Synse is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

Synse is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Synse.  If not, see <http://www.gnu.org/licenses/>.
"""
from nose.plugins.attrib import attr  # noqa

import testtools
import requests
import json
from time import sleep


class TestEndpoints(testtools.TestCase):

    def test_test_endpoint(self):
        """ Hit the /test endpoint and confirm that it returns
        the correct response
        """
        r = requests.get('http://synse-prometheus:9243/test')
        self.assertEqual(r.status_code, 200)
        response = json.loads(r.text)
        self.assertEqual(response['status'], 'ok')

    def test_metrics_endpoint(self):
        """ Hit the /metrics endpoint twice, confirming that it returns
        different results over time.
        """
        first_response = requests.get('http://synse-prometheus:9243/metrics')
        self.assertEqual(first_response.status_code, 200)

        # Wait for the prometheus metrics to update.
        # FIXME -- There must be a better way to handle the timing here
        sleep(20)
        second_response = requests.get('http://synse-prometheus:9243/metrics')
        self.assertEqual(second_response.status_code, 200)
        self.assertNotEqual(first_response.text, second_response.text)


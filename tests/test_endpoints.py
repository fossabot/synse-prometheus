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
import testtools
from requests import get


class TestEndpoints(testtools.TestCase):

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
        response = self.request('http://synse-prometheus:9243/test').json()
        self.assertEqual(response['status'], 'ok')

    def test_metrics_endpoint(self):
        """ Hit the /metrics endpoint twice, confirming that it returns
        different results after more data has been collected.
        """
        first_response = self.request('http://synse-prometheus:9243/metrics')

        # Hit the test endpoint in order to
        # update the results from the metrics endpoint
        self.request('http://synse-prometheus:9243/test')

        second_response = self.request('http://synse-prometheus:9243/metrics')
        self.assertNotEqual(first_response.text, second_response.text)

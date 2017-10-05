#!/usr/bin/env python
""" GraphQL Frontend

    Author:  Thomas Rampelberg
    Date:    2/24/2017

    \\//
     \/apor IO
"""

from synse_prometheus import app, config


if __name__ == '__main__':
    config.parse_args()
    app.setup_logging()
    app.main()

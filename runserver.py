#!/usr/bin/env python
""" GraphQL Frontend

    Author:  Thomas Rampelberg
    Date:    2/24/2017

    \\//
     \/apor IO
"""

from prometheus_endpoint import config
from prometheus_endpoint import main, setup_logging


if __name__ == '__main__':
    config.parse_args()
    setup_logging()
    main()

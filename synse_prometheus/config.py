""" Configuration

    Author:  Thomas Rampelberg
    Date:    2/24/2017

    \\//
     \/apor IO
"""

import configargparse

parser = configargparse.ArgParser(default_config_files=[
    "/code/config.yml"
])
parser.add('-c', '--my-config', is_config_file=True, help='config file path')
parser.add(
    '--port',
    env_var='PORT',
    default=9243,
    help='Port to listen on.')
parser.add(
    '--synse-graphql',
    env_var='SYNSE_GRAPHQL',
    default='synse-graphql:5001',
    help='Path to synse-grapql to use. example: "localhost:5001"')

options = None


def parse_args(opts=None):
    global options
    options = vars(parser.parse_args(opts))

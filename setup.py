
VERSION = "1.0.0"

config = {
    'name': 'synse_prometheus',
    'version': VERSION,
    'author': 'Thomas Rampelberg',
    'author_email': 'thomasr@vapor.io',
    'test_suite': 'nose.collector'
}

if __name__ == "__main__":
    from setuptools import setup

    setup(**config)

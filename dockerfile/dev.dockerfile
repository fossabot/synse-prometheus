FROM vaporio/synse-prometheus

RUN apk add --no-cache \
  build-base \
  curl

RUN pip install --upgrade \
  pip \
  setuptools \
  tox

CMD ["bin/sleep.sh"]

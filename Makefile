# ------------------------------------------------------------------------
#  \\//
#   \/aporIO - Vapor Synse-prometheus
#
#  Build Vapor synse-prometheus docker images from the current directory.
#
#  Author: Klemente Gilbert-Espada (klemente@vapor.io)
#  Date:   27 April 2017
# ------------------------------------------------------------------------

IMG_NAME := vaporio/synse-prometheus
PKG_VER := $(shell python synse_prometheus/__init__.py)
export GIT_VER := $(shell /bin/sh -c "git log --pretty=format:'%h' -n 1 || echo 'none'")

.PHONY: build
build:
	docker build -f dockerfile/base.dockerfile \
		-t ${IMG_NAME}:latest \
		-t ${IMG_NAME}:${PKG_VER} \
		-t ${IMG_NAME}:${GIT_VER} .

.PHONY: test
test:
	docker-compose -f compose/base.yml -f compose/dev.yml -f compose/test.yml up \
	  --build \
	  --abort-on-container-exit \
	  --exit-code-from synse-prometheus

.PHONY: dev
dev:
	docker-compose -f compose/base.yml -f compose/dev.yml up \
		-d \
		--build
	-docker exec -it synse-prometheus /bin/sh
	$(MAKE) down

.PHONY: run
run:
	docker-compose -f compose/base.yml -f compose/dev.yml -f compose/run.yml up \
		-d \
		--build

.PHONY: circleci
circleci:
	docker-compose -f compose/base.yml -f compose/test.yml -f compose/test-circleci.yml up \
	  --build \
	  --abort-on-container-exit \
	  --exit-code-from synse-prometheus

.PHONY: down
down:
	docker-compose -f compose/base.yml -f compose/dev.yml down

.PHONY: logs
logs:
	docker-compose -f compose/base.yml -f compose/dev.yml logs

.PHONY: config-volume
config-volume:
	docker volume create source
	docker run -v config:/scratch --name helper busybox true
	docker cp config/bmc.json helper:/scratch
	docker cp config/config.json helper:/scratch
	docker rm helper

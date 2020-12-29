.PHONY: default
default: install

.PHONY: install
install:
	pip install pipenv
	pipenv install --deploy --dev

.PHONY: lint
lint:
	pipenv run pre-commit run

.PHONY: lint-all
lint-all:
	pipenv run pre-commit run --all-files

.PHONY: test
test:
	pipenv run python -m pytest

.PHONY: shell
shell:
	pipenv shell

.PHONY: run
run:
	pipenv run python -m advent_of_code_2020

.PHONY: docker-build
docker-build:
	docker build . -t advent_of_code_2020:test

.PHONY: docker-run
docker-run:
	docker run --rm advent_of_code_2020:test

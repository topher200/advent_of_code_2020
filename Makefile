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
	pipenv run pytest

.PHONY: shell
shell:
	pipenv shell

.PHONY: run
run:
	pipenv run python advent_of_code_2020/__main__.py

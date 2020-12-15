.PHONY: default
default: install

.PHONY: install
install:
	pipenv install --dev

.PHONY: lint
lint:
	pipenv run pre-commit run

.PHONY: test
test:
	pipenv run pytest

.PHONY: shell
shell:
	pipenv shell

.PHONY: run
run:
	pipenv run python advent_of_code_2020/__main__.py

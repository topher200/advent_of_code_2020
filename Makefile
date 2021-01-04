.PHONY: install
install:
	pip install pipenv
	pipenv install --deploy --dev

.PHONY: test
test:
	pipenv run pre-commit run

.PHONY: test-full
test-full:
	pipenv run pre-commit run --hook post-commit --all-files

.PHONY: shell
shell:
	pipenv shell

.PHONY: docker-build
docker-build:
	docker build . -t advent_of_code_2020:test

.PHONY: docker-run
docker-run:
	docker run --rm advent_of_code_2020:test

.PHONY: run
run:
	pipenv run python -m advent_of_code_2020

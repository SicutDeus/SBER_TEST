WORKDIR = app/
TESTS_DIR = tests/

.PHONY: format lint test all

format:
	black ${WORKDIR}
	isort ${WORKDIR}

lint:
	flake8 ${WORKDIR}

test:
	python -m unittest discover -s ${TESTS_DIR}

update_cov:
	coverage run -m unittest discover -s tests
	coverage report
	coverage html
	python -m update_coverage_readme

tests_folder_check:
	black ${TESTS_DIR}
	isort ${TESTS_DIR}
	flake8 ${TESTS_DIR}

all: format lint test update_cov

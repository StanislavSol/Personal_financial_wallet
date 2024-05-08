install:
	poetry install

wallet:
	poetry run wallet

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*whl

package-install-force:
	python3 -m pip install --user --force-reinstall dist/*.whl


lint:
	poetry run flake8

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov

test-coverage:
	poetry run pytest --cov=wallet  --cov-report xml

.PHONY: install test lint selfcheck check build

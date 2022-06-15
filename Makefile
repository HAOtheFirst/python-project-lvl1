install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish: build
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install build brain-even
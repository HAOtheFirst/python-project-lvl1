install: #  Environment initialization
	poetry install

brain-games: # Welcome
	poetry run brain-games

build: # Project build
	poetry build

publish: # Publish Project
	poetry publish --dry-run

package-install: # installing a project from the operating system
	python3 -m pip install --user dist/*.whl


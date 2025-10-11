install:
	poetry install
project:
	poetry run project
.PHONY: build publish
build:
	poetry build
publish:
	poetry publish --dry-run
.PHONY: package-install
packege-install:
	python3 -m pip install dist/*.whl

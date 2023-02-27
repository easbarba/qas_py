deps:
	poetry install

test:
	poetry run pytest

.PHONY := deps test

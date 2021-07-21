debug:
	pytest tests/tests_*.py --pdb

test:
	pytest tests/tests_*.py
pretty:
	black tests/tests_*.py
	isort tests/tests_*.py
	black pysondb/*.py
	isort pysondb/*.py

all: pretty test

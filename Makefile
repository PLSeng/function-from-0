install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

test:
	python -m pytest -vv tests/test_*.py

lint:
	pylint --disable=R,C,E1120 *.py

all: install format lint test
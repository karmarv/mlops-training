install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv modrunner_test.py

format:
	black *.py


lint:
	pylint --disable=R,C modrunner.py

all: install lint test

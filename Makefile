.PHONY: install run test

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	PYTHONPATH=. pytest -v

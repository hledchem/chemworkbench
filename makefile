.PHONY: install dev test lint run

install:
	poetry install

dev:
	poetry shell

test:
	poetry run pytest -q

lint:
	poetry run black --check .
	poetry run isort --check-only .

run:
	poetry run uvicorn app.main:app --reload

PROJECT_NAME:=dynamic_kg_extractor
EXECUTER:=uv run

all: format lint type security test

init:
	git init
	$(EXECUTER) uv sync
	$(EXECUTER) pre-commit install

clean:
	rm -rf .mypy_cache .pytest_cache .coverage htmlcov
	$(EXECUTER) ruff clean

format:
	$(EXECUTER) ruff format .

lint:
	$(EXECUTER) ruff check . --fix

test:
	$(EXECUTER) pytest --cov-report term-missing --cov-report html --cov $(PROJECT_NAME)/

type:
	$(EXECUTER) mypy .

security:
	$(EXECUTER) bandit -r $(PROJECT_NAME)/
	$(EXECUTER) pip-audit


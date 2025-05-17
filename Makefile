.PHONY: help test lint format build clean docker

help:
	@echo "Available commands:"
	@echo "  test		- Run tests with pytest"
	@echo "  lint		- Run linter (flake8)"
	@echo "  format	  - Format code with black and isort"
	@echo "  build	   - Build package with poetry"
	@echo "  clean	   - Remove build artifacts"
	@echo "  docker	  - Build and run tests in Docker"

test:
	poetry run pytest tests/

lint:
	poetry run flake8 byterun/ tests/

format:
	poetry run black byterun/ tests/
	poetry run isort byterun/ tests/

build:
	poetry build

clean:
	rm -rf dist/ .pytest_cache/ __pycache__ .mypy_cache/ coverage.xml htmlcov .coverage*

docker:
	docker build -t byterun .
	docker run --rm byterun make test
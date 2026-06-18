install:
	uv sync

lint:
	uv run ruff check .

lint-fix:
	uv run ruff check . --fix

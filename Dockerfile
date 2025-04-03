FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS builder


WORKDIR /app
COPY pyproject.toml uv.lock /app/

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

#production
FROM python:3.13-slim-bookworm AS production
COPY data /app/data
COPY --from=builder --chown=app:app /app /app

COPY onto_to_kg_dynamic /app/onto_to_kg_dynamic
COPY exp.py /app/exp.py
ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app
CMD ["python", "exp.py"]


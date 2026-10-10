FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8080

WORKDIR /app
COPY pyproject.toml README.md serve_http.py ./
COPY src ./src
RUN pip install .

CMD ["python", "serve_http.py"]

FROM python:3.10-slim

WORKDIR /app

# System dependencies for scientific computing if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
COPY README.md .
COPY src/ src/

RUN pip install --no-cache-dir .

# Default command
CMD ["python", "-c", "import stateda; print('StatEDA-Explorer environment ready.')"]
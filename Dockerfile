FROM python:3.11

WORKDIR /var/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk upgrade \
    && apk add --no-cache  \
    python3-dev


RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python
ENV PATH="${PATH}:/etc/poetry/bin"

COPY poetry.toml poetry.toml
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN set -ex && poetry install --no-root

COPY . .

# CMD ["python", "/var/app/src/__main__.py"]
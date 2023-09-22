FROM python:3.10

WORKDIR /var/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apt-get update \
#     && apk upgrade \
#     && apk add --no-cache  \
#     python3-dev

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python
ENV PATH="${PATH}:/etc/poetry/bin"

COPY poetry.toml poetry.toml
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN set -ex && poetry install --no-root

COPY . .

RUN ["cp", "/var/app/.env.example", "/var/app/.env"]

# CMD [ "python", "src/__main__.py" ]
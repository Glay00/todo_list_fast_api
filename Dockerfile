FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.7.1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR=/var/cache/pypoetry

WORKDIR opt/app

RUN apk update && apk upgrade && \
    apk add --no-cache ttf-dejavu gcc musl-dev bash zlib-dev jpeg-dev cairo-dev pango-dev gdk-pixbuf-dev

RUN pip install "poetry-core" "poetry==${POETRY_VERSION}"

COPY ./src ./src

COPY ./poetry.lock ./pyproject.toml ./alembic.ini /opt/app/
COPY /docker/ /opt/app/docker/

RUN poetry install --no-root

ENV PYTHONPATH "${PYTHONPATH}:/opt/app"

RUN chmod a+x docker/*.sh

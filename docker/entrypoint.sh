#!/usr/bin/env bash

alembic upgrade head
cd src
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
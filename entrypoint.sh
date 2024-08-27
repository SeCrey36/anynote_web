#!/bin/sh

#Setting for stopping after getting an error
set -e

RUN_MANAGE_PY='poetry run python manage.py'

echo 'Collect static...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Migrations...'
$RUN_MANAGE_PY makemigrations --no-input
$RUN_MANAGE_PY migrate --no-input

$RUN_MANAGE_PY runserver 0.0.0.0:8000
#exec "$@"
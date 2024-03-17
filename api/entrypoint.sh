#!/bin/sh

echo "STARTING MIGRATION: "

python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "FINISHED"


exec "$@"
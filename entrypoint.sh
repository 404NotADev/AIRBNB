#!/bin/bash
set -e

sleep 4
#python manage.py makemigrations
python manage.py migrate
# python manage.py runserver 0.0.0.0:8000


exec "$@"
chmod +x entrypoint.sh
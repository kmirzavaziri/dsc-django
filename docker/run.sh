#!/bin/bash
python /app/manage.py makemigrations
python /app/manage.py migrate
gunicorn --bind 0.0.0.0:8001 --workers 1 main.wsgi:application

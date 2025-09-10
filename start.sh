#!/bin/sh
# Run database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start the app with Gunicorn, binding to the PORT Railway provides
gunicorn config.wsgi --bind 0.0.0.0:$PORT

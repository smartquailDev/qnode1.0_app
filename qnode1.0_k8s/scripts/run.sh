#!/bin/sh

set -e
APP_PORT=${PORT:-9000}
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"smartquail.info@gmail.com"}


python manage.py migrate --noinput
python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
python manage.py collectstatic --noinput 

uwsgi  --workers 4  --ini uwsgi_prod.ini

#python manage.py listen_port25 --noinput

#gunicorn --worker-tmp-dir /dev/shm  --bind "0.0.0.0:${APP_PORT}"  qnode0_app.wsgi:application 


#!/usr/bin/env python3

python manage.py makemigrations

until python manage.py migrate; do
  sleep 2
  echo "Retrying to migrate db ... ";
done

python manage.py shell < init_admin.py

python manage.py collectstatic --noinput

echo "Django App is ready ....";

# python manage.py runserver 0.0.0.0:8000


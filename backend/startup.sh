#!/usr/bin/env python3

python manage.py makemigrations

until python manage.py migrate; do
  sleep 2
  echo "Retrying ....";
done

python manage.py shell < init_admin.py

python manage.py makemigrations
python manage.py migrate

echo "Django is ready ....";

python manage.py runserver 0.0.0.0:8000


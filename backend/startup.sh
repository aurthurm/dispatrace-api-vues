echo "Running Django Migrations ...";

python ./manage.py makemigrations

until python ./manage.py migrate; do
  sleep 2
  echo "Retrying to migrate db ... ";
done

python ./manage.py shell < init_admin.py

echo "Django App is ready ....";
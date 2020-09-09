echo "Running Django Migrations ...";

python /app/backend/manage.py makemigrations

until python /app/backend/manage.py migrate; do
  sleep 2
  echo "Retrying to migrate db ... ";
done

python /app/backend/manage.py shell < init_admin.py

echo "Django App is ready ....";
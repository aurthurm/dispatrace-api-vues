## Run these commands

# 1.
docker-compose run django django-admin startproject dispatrace .

# 2. connect the db
if 'DB_NAME' in os.environ:
    # Running the Docker image
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASS'],
            'HOST': os.environ['DB_SERVICE'],
            'PORT': os.environ['DB_PORT']
        }
    }
else:
    # Building the Docker image
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# 3.
ALLOWED_HOSTS = ['*']

# 4.
# SmartWorks -formerly dispatrace

1. clone this repo with git clone http://repo-link
2. in the root dir run: docker-compose up
3. username and password: dispatrace:dispatrace
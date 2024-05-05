# Django Rest Framework

## Instalación

```bash
pip install djangorestframework

pip install psycopg2-binary

pip install dj-database-url

# Add these dependencies to your requirements.txt file:
pip freeze > requirements.txt

```

## Configuración 

```python
INSTALLED_APPS = [
    ...
    'inventory', # Aplicación 
    'rest_framework',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('DB_NAME'),
        'USER': environ.get('DB_USER'),
        'PASSWORD': environ.get('DB_PASSWORD'),
        'HOST': environ.get('DB_HOST'),
        'PORT': environ.get('DB_PORT'),
    }
}

```
## Instalar Cloudinary

```bash
pip install cloudinary
```

## Instalar Python Dotenv

```bash
pip install python-dotenv
```

## Configurar Cloudinary

```python
from cloudinary import config
from dotenv import load_dotenv
from os import environ

load_dotenv()
...
INSTALLED_APPS = [
    ...
    'cloudinary',
    ...
]

config (
    cloud_name = environ.get
    ('CLOUDINARY_CLOUD_NAME'),
    api_key = environ.get
    ('CLOUDINARY_API_KEY'),
    api_secret = environ.get
    ('CLOUDINARY_API_SECRET')
)
...
```

## Migraciones "Ejecutar"

```bash

python manage.py makemigrations
python manage.py migrate 
```
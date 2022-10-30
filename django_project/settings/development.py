from .base import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'django_project',
        'USER': 'root',
        'PASSWORD': 'Masterkey1',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
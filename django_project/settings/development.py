from .base import *

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
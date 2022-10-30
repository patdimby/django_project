from .base import *

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'django_project',
        'USER': 'root',
        'PASSWORD': 'Masterkey1',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
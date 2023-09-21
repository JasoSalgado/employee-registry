from decouple import config
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'drfuser',
        'PASSWORD': 'drfuser',
        'HOST': 'localhost',
        'PORT': 5432,        
    }
}

STATIC_URL = 'static/'
STATICFILES_DIRS = ['static/']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
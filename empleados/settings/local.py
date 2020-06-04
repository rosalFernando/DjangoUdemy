

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []





# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
      #  'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME':'dbempleado',
        'USER':'fernando',
        'PASSWORD':'fernando',
        'HOST':'localhost',
        'PORT':'5432',

    }
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

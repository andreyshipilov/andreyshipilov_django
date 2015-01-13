"""
Development settings.

"""
from os.path import join
from base import *


DEBUG = True

TEMPLATE_DEBUG = DEBUG

WSGI_APPLICATION = 'andreyshipilov.wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, '../andreyshipilov.db'),
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

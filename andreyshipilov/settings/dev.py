"""
Development settings.

"""
from os.path import join
from base import *


DEBUG = True

THUMBNAIL_DEBUG = DEBUG

TEMPLATES[0]['OPTIONS']['debug'] = True

WSGI_APPLICATION = 'andreyshipilov.wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, '../dev.db'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

COMPRESS_ENABLED = True

COMPRESS_REBUILD_TIMEOUT = 1

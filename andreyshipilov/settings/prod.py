"""
Production settings

"""
from common import *


DATABASE_STATEMENT_TIMEOUT = 2 * 60 * 1000

WSGI_APPLICATION = 'wsgi.prod.application'

ALLOWED_HOSTS = ['.andreyshipilov.com']

COMPRESS_CSS_FILTERS += [
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_JS_FILTERS += [
    'compressor.filters.jsmin.JSMinFilter',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/home/ovaladmin/tmp/cache/dev.oneoval',
    }
}

ADMINS = (
    ('Andrey', 'a@andreyshipilov.com'),
)

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_PORT = '25'
DEFAULT_FROM_EMAIL = 'info@andreyshipilov.com'
SERVER_EMAIL = 'info@andreyshipilov.com'
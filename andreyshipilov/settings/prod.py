"""
Production settings

"""
from base import *

# DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": DATABASE_NAME_USER,
        "USER": DATABASE_NAME_USER,
        "PASSWORD": DATABASE_PASSWORD,
    }
}

DATABASE_STATEMENT_TIMEOUT = 2 * 60 * 1000

WSGI_APPLICATION = 'wsgi.prod.application'

ALLOWED_HOSTS = ['.andreyshipilov.com']

COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
    'compressor.filters.jsmin.JSMinFilter',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/home/tezro/sockets/memcached.sock',
    }
}

ADMINS = (
    ('Andrey', 'a@andreyshipilov.com'),
)

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_PORT = '25'
DEFAULT_FROM_EMAIL = 'a@andreyshipilov.com'
SERVER_EMAIL = 'a@andreyshipilov.com'

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', '/home/tezro/django_projects/andreyshipilov/gems/bin/sass --scss {infile} {outfile}'),
)

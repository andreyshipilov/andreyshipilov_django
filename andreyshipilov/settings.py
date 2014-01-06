# -*- coding: utf-8 -*-
import re
import sys
from os.path import join, abspath, dirname

from secret_info import *



PROJECT_DIR = dirname(__file__)

# Paths to add on os.path
PATHS = (
    abspath(join(PROJECT_DIR, 'apps')),
)
[sys.path.insert(0, i) if i not in sys.path else None for i in PATHS]


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Andrey', 'a@andreyshipilov.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME_USER,
        'USER': DATABASE_NAME_USER,
        'PASSWORD': DATABASE_PASSWORD,
    }
}
DATABASE_STATEMENT_TIMEOUT = 2 * 60 * 1000
CACHES = {
    'default': {
#        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#        'LOCATION': '/home/tezro/django_projects/andreyshipilov/django_cache',
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/home/tezro/__memcached.sock',
    }
}

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_PORT = '25'
DEFAULT_FROM_EMAIL = "error@andreyshipilov.ru"
SERVER_EMAIL = "error@andreyshipilov.ru"

TIME_ZONE = 'Australia/Adelaide'
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', u'English'),
    ('ru', u'Русский'),
)
SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = join(PROJECT_DIR, 'static/media')
MEDIA_URL = '/m/'
STATIC_ROOT = join(PROJECT_DIR, 'static')
STATIC_URL = '/s/'
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

SECRET_KEY = '&*=gtkh3a_e@u76r0!$h26(w97ba+3r__jzbcc80)l#o6iaxy#'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'andreyshipilov.urls'

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'me.context_processors.socials',
)

TEMPLATE_DIRS = (
    join(PROJECT_DIR, 'templates')
)

WSGI_APPLICATION = 'andreyshipilov.wsgi.application'

INSTALLED_APPS = (
    'localeurl',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.markup',

    'me',
    'cv',

    'compressor',
    'debug_toolbar',
    'hvad',
    'robots',
    'south',
    #'rosetta',
    'typogrify',
)

# Localeurl
PREFIX_DEFAULT_LOCALE = False
LOCALE_INDEPENDENT_PATHS = (
    re.compile('^/everyone-tweet/'),
    re.compile('^/(i|lj|:3)/'),
)

# Sorl
THUMBNAIL_ENABLE_CACHING = False
THUMBNAIL_QUALITY = 80

# Compressor
COMPRESS_OUTPUT_DIR = 'zip'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.cssmin.CSSMinFilter',
    'compressor.filters.css_default.CssAbsoluteFilter',
]

# Debug Toolbar and shit
INTERNAL_IPS = ('127.0.0.1',)


# Local settings
try:
    from local_settings import *
except ImportError:
    pass

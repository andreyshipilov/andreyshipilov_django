# -*- coding: utf-8 -*-

import os
import re
import sys
from django.conf.global_settings import (TEMPLATE_CONTEXT_PROCESSORS,
                                         STATICFILES_FINDERS)
from secret_info import *


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = '&*=gtkh3a_e@u76r0!$h26(w97ba+3r__jzbcc80)l#o6iaxy#'

SITE_ID = 1

DJANGO_APPS = (
    'localeurl',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'compressor',
    'south',
    'django_reset',
    'robots',
    'clear_cache',
    'typogrify',
    'markdown_deux',
    'sorl.thumbnail',
    # 'sitetree',
    'bourbon',
    'axes',
    'compressor',
    'hvad',
    'meta',
)

LOCAL_APPS = (
    'me',
    'cv',
    'django_cleanup',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'localeurl.middleware.LocaleURLMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.FailedLoginMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'me.context_processors.socials',
)

ROOT_URLCONF = 'andreyshipilov.urls'

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', u'English'),
    ('ru', u'Русский'),
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static_root')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, '../media_root')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, '../locale'),
)

"""
Apps related settings.
"""

# Localeurl
PREFIX_DEFAULT_LOCALE = False
LOCALE_INDEPENDENT_PATHS = (
    re.compile('^/everyone-tweet/'),
    re.compile('^/(i|lj|:3)/'),
)

# Sorl
THUMBNAIL_QUALITY = 90
THUMBNAIL_UPSCALE = False

# Django compressor settings
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# Django Axes
AXES_LOGIN_FAILURE_LIMIT = 10
AXES_COOLOFF_TIME = 0.08  # ~5 minutes.

# Django Meta
META_SITE_PROTOCOL = 'http'
META_SITE_DOMAIN = 'www.andreyshipilov.com'
META_SITE_TYPE = 'website'
META_DEFAULT_KEYWORDS = ['Andrey Shipilov', 'Shipilov', 'web developer',
                         'web design', 'website', 'freelance', 'python',
                         'django', 'html', 'javascript', 'sql', 'css',
                         'Bear On Unicycle', 'Adelaide']
META_INCLUDE_KEYWORDS = META_DEFAULT_KEYWORDS
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True

# Local settings
try:
    from local_settings import *
except ImportError:
    pass

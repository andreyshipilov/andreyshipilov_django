import os
import site

site.addsitedir('/home/tezro/django_projects/andreyshipilov/andreyshipilov_venv/lib/python2.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'andreyshipilov.settings.prod'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

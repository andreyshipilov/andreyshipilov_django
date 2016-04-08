import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "andreyshipilov.settings.prod")
os.environ['GEM_HOME'] = '/home/tezro/django_projects/andreyshipilov/gems'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

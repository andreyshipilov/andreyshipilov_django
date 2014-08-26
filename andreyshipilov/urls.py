from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.contrib import admin

from localeurl.sitemaps import LocaleurlSitemap
from localeurl.models import patch_reverse

from me.models import Project


patch_reverse()
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^le_admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^$', 'me.views.index', name="home"),
    url(r'^projects/$', 'me.views.projects', name='projects'),
    url(r'^projects/(?P<slug>[-\w]+)/$', 'me.views.type_or_project', name='type_or_project'),
    url(r'^cv/$', 'cv.views.cv', name='cv'),
    url(r'^everyone-tweet/$', 'me.views.everyone_tweet', name='everyone_tweet'),

    (r'^robots.txt$', include('robots.urls')),
    (r'^localeurl/', include('localeurl.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


class ProjectsSitemap(LocaleurlSitemap):
    """
    Multilingual sitemaps
    """
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return Project.get_published()


sitemaps = {
    'projects-ru': ProjectsSitemap('ru'),
    'projects-en': ProjectsSitemap('en'),
}
urlpatterns += patterns('',
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
)

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin

# from localeurl.sitemaps import LocaleurlSitemap

from me.models import Project
import me.views
import cv.views


admin.autodiscover()
urlpatterns = []

if settings.DEBUG:
    import debug_toolbar


    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^le_admin/', include(admin.site.urls)),
    url(r'^le_admin/rosetta/', include('rosetta.urls')),

    url(r'^everyone-tweet/$', me.views.everyone_tweet, name='everyone_tweet'),
    url(r'^robots.txt', include('robots.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^$', me.views.home, name='home'),
    url(r'^projects/$', me.views.projects, name='projects'),
    url(r'^projects/(?P<slug>[-\w]+)/$', me.views.type_or_project, name='type_or_project'),
    url(r'^cv/$', cv.views.cv, name='cv'),
    prefix_default_language=False
)


# class ProjectsSitemap(LocaleurlSitemap):
#     """
#     Multilingual sitemaps
#     """
#     priority = 0.6
#     changefreq = 'monthly'
#
#     def items(self):
#         return Project.get_published()


# sitemaps = {
#     'projects-ru': ProjectsSitemap('ru'),
#     'projects-en': ProjectsSitemap('en'),
# }
# urlpatterns += [
#     url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap',
#         {'sitemaps': sitemaps}),
# ]

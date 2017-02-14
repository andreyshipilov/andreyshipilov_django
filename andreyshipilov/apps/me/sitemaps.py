from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Project


class ProjectSitemap(Sitemap):
    """
    Projects sitemaps.
    """
    priority = 0.7
    changefreq = 'monthly'
    i18n = True

    def items(self):
        return Project.get_published()


class StaticViewSitemap(Sitemap):
    """
    Static views sitemaps.
    """
    priority = 0.6
    changefreq = 'monthly'
    i18n = True

    def items(self):
        return ['home', 'projects', 'cv', 'everyone_tweet']

    def location(self, item):
        return reverse(item)

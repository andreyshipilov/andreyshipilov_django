# -*- coding: utf-8 -*-
from django.db import models


class Position(models.Model):
    company_name = models.CharField(max_length=50,)
    company_website = models.URLField(max_length=100, blank=True,)
    company_alternate_name = models.CharField(max_length=50, blank=True,)
    company_alternate_website = models.URLField(max_length=100, blank=True,)
    company_location = models.CharField(max_length=50, blank=True,)

    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True,)
    show_only_years = models.BooleanField(default=False,)

    title = models.CharField(max_length=50,)
    description = models.TextField(help_text='')

    class Meta:
        ordering = ('-date_start', '-date_end',)

    def __unicode__(self):
        return "{0}, {1}".format(self.title, self.company_name)

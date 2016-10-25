# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache
from django.utils.translation import ungettext

from sorl.thumbnail import ImageField
from pytils.translit import slugify
from os.path import splitext
from hvad.models import TranslatableModel, TranslatedFields
from any_imagefield.models import AnyImageField as ImageField


class Social(models.Model):
    title = models.CharField(max_length=100, )
    link = models.URLField(max_length=300, )
    image = ImageField(
        upload_to=lambda instance, filename: "social_icons/%s%s" %
                                             (slugify(
                                                 instance.title.lower()) or
                                              'icon',
                                              splitext(filename)[1].lower()),
    )

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title


class ProjectType(TranslatableModel):
    slug = models.SlugField(max_length=200)
    translations = TranslatedFields(
        title=models.CharField(max_length=250),
    )

    def __unicode__(self):
        return self.lazy_translation_getter('title', )

    def save(self, *args, **kwargs):
        cache.clear()
        super(ProjectType, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('type_or_project', (), {'slug': self.slug})


class Project(TranslatableModel):
    is_published = models.BooleanField(default=False, db_index=True)
    is_alive = models.BooleanField(default=False, db_index=True,
                                   help_text=u'Screenshots will be shown if is not alive.')
    is_notable = models.BooleanField(default=False, help_text=u'Will be shown in CV.', )
    has_archive = models.BooleanField(default=False, db_index=True)
    date = models.DateField(db_index=True, )
    slug = models.SlugField(max_length=200, )
    link = models.URLField(max_length=500, blank=True)
    project_type = models.ManyToManyField(ProjectType, blank=True, null=True)
    image = ImageField(
        blank=True, max_length=400, help_text='Save first.',
        upload_to=lambda instance, filename: "project/%s/%s-preview%s" %
                                             (instance.slug, instance.slug,
                                              splitext(filename)[1].lower()),
    )

    translations = TranslatedFields(
        explict_title=models.CharField(max_length=250),
        title=models.CharField(max_length=250, blank=True),
        verbose_link=models.CharField(max_length=100, blank=True),
        verbose_link_text=models.CharField(max_length=100, blank=True),
        text=models.TextField(blank=True),
        client=models.TextField(blank=True),
    )

    class Meta:
        ordering = ('-date',)

    def __unicode__(self):
        return self.lazy_translation_getter('title', str(self.date))

    def save(self, *args, **kwargs):
        cache.clear()
        super(Project, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('type_or_project', (), {'slug': self.slug})

    @staticmethod
    def get_published():
        return Project.objects.language().filter(is_published=True)

    @staticmethod
    def get_notable():
        return Project.get_published().filter(is_notable=True)

    def get_screenshot_count_string(self):
        count = self.screenshot_set.count()

        if count:
            return "{0} {1}".format(count,
                                    ungettext("screenshot", "screenshots", count))
        else:
            return ""


class Screenshot(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=100, blank=True)
    image = ImageField(
        max_length=400,
        upload_to=lambda instance,
                         filename: "project/%s/screenshots/%s-screenshot%s" % \
                                   (instance.project.slug, instance.project.slug,
                                    splitext(filename)[1].lower()),
    )

    class Meta:
        ordering = ('pk',)

    def save(self, *args, **kwargs):
        cache.clear()
        super(Screenshot, self).save(*args, **kwargs)


class Participant(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=250, blank=True),
        link=models.URLField(max_length=500, blank=True),
    )

    def __unicode__(self):
        return self.title or 'Participant'


class Role(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=250, blank=True),
    )

    def __unicode__(self):
        return self.title or 'Role'


class Participation(models.Model):
    project = models.ForeignKey(Project)
    participant = models.ForeignKey(Participant)
    role = models.ManyToManyField(Role)

    def __unicode__(self):
        return 'Participation'


class Tweet(models.Model):
    text = models.CharField(max_length=160, )
    date = models.DateTimeField(auto_now_add=True, )
    country = models.CharField(blank=True, max_length=100, )
    latitude = models.DecimalField(max_digits=20, decimal_places=17, default=0.0)
    longitude = models.DecimalField(max_digits=20, decimal_places=17, default=0.0)

    class Meta:
        ordering = ('-date',)

    def __unicode__(self):
        return self.text

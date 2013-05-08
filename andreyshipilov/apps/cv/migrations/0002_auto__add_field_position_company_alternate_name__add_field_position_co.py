# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Position.company_alternate_name'
        db.add_column('cv_position', 'company_alternate_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'Position.company_alternate_website'
        db.add_column('cv_position', 'company_alternate_website',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Position.show_only_years'
        db.add_column('cv_position', 'show_only_years',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Position.company_alternate_name'
        db.delete_column('cv_position', 'company_alternate_name')

        # Deleting field 'Position.company_alternate_website'
        db.delete_column('cv_position', 'company_alternate_website')

        # Deleting field 'Position.show_only_years'
        db.delete_column('cv_position', 'show_only_years')


    models = {
        'cv.position': {
            'Meta': {'ordering': "('-date_start', '-date_end')", 'object_name': 'Position'},
            'company_alternate_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'company_alternate_website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'company_location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'company_website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_only_years': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cv']
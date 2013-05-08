# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Position.date_end'
        db.alter_column('cv_position', 'date_end', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Position.date_end'
        raise RuntimeError("Cannot reverse this migration. 'Position.date_end' and its values cannot be restored.")

    models = {
        'cv.position': {
            'Meta': {'ordering': "('-date_start', '-date_end')", 'object_name': 'Position'},
            'company_alternate_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'company_alternate_website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'company_location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'company_website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_only_years': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cv']
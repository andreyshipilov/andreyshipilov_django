# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Position'
        db.create_table('cv_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('company_website', self.gf('django.db.models.fields.URLField')(max_length=100, blank=True)),
            ('company_location', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('date_start', self.gf('django.db.models.fields.DateField')()),
            ('date_end', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('cv', ['Position'])


    def backwards(self, orm):
        # Deleting model 'Position'
        db.delete_table('cv_position')


    models = {
        'cv.position': {
            'Meta': {'ordering': "('-date_start', '-date_end')", 'object_name': 'Position'},
            'company_location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'company_website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cv']
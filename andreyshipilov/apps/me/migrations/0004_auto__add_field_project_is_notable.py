# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.is_notable'
        db.add_column('me_project', 'is_notable',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.is_notable'
        db.delete_column('me_project', 'is_notable')


    models = {
        'me.participant': {
            'Meta': {'object_name': 'Participant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'me.participanttranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ParticipantTranslation', 'db_table': "'me_participant_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['me.Participant']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        'me.participation': {
            'Meta': {'object_name': 'Participation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['me.Participant']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['me.Project']"}),
            'role': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['me.Role']", 'symmetrical': 'False'})
        },
        'me.project': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Project'},
            'date': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'has_archive': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '400', 'blank': 'True'}),
            'is_alive': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_notable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'project_type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['me.ProjectType']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'})
        },
        'me.projecttranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ProjectTranslation', 'db_table': "'me_project_translation'"},
            'client': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'explict_title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['me.Project']"}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'verbose_link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'verbose_link_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'me.projecttype': {
            'Meta': {'object_name': 'ProjectType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'})
        },
        'me.projecttypetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ProjectTypeTranslation', 'db_table': "'me_projecttype_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['me.ProjectType']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'me.role': {
            'Meta': {'object_name': 'Role'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'me.roletranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'RoleTranslation', 'db_table': "'me_role_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['me.Role']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        'me.screenshot': {
            'Meta': {'object_name': 'Screenshot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '400'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['me.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'me.social': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Social'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'me.tweet': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Tweet'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '20', 'decimal_places': '17'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '20', 'decimal_places': '17'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        }
    }

    complete_apps = ['me']
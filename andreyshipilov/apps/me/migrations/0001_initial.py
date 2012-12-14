# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Social'
        db.create_table('me_social', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=300)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('me', ['Social'])

        # Adding model 'ProjectTypeTranslation'
        db.create_table('me_projecttype_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['me.ProjectType'])),
        ))
        db.send_create_signal('me', ['ProjectTypeTranslation'])

        # Adding unique constraint on 'ProjectTypeTranslation', fields ['language_code', 'master']
        db.create_unique('me_projecttype_translation', ['language_code', 'master_id'])

        # Adding model 'ProjectType'
        db.create_table('me_projecttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
        ))
        db.send_create_signal('me', ['ProjectType'])

        # Adding model 'ProjectTranslation'
        db.create_table('me_project_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('explict_title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('client', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['me.Project'])),
        ))
        db.send_create_signal('me', ['ProjectTranslation'])

        # Adding unique constraint on 'ProjectTranslation', fields ['language_code', 'master']
        db.create_unique('me_project_translation', ['language_code', 'master_id'])

        # Adding model 'Project'
        db.create_table('me_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('is_alive', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('has_archive', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('date', self.gf('django.db.models.fields.DateField')(db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=400, blank=True)),
        ))
        db.send_create_signal('me', ['Project'])

        # Adding M2M table for field project_type on 'Project'
        db.create_table('me_project_project_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['me.project'], null=False)),
            ('projecttype', models.ForeignKey(orm['me.projecttype'], null=False))
        ))
        db.create_unique('me_project_project_type', ['project_id', 'projecttype_id'])

        # Adding model 'Screenshot'
        db.create_table('me_screenshot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['me.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=400)),
        ))
        db.send_create_signal('me', ['Screenshot'])

        # Adding model 'ParticipantTranslation'
        db.create_table('me_participant_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['me.Participant'])),
        ))
        db.send_create_signal('me', ['ParticipantTranslation'])

        # Adding unique constraint on 'ParticipantTranslation', fields ['language_code', 'master']
        db.create_unique('me_participant_translation', ['language_code', 'master_id'])

        # Adding model 'Participant'
        db.create_table('me_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('me', ['Participant'])

        # Adding model 'RoleTranslation'
        db.create_table('me_role_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['me.Role'])),
        ))
        db.send_create_signal('me', ['RoleTranslation'])

        # Adding unique constraint on 'RoleTranslation', fields ['language_code', 'master']
        db.create_unique('me_role_translation', ['language_code', 'master_id'])

        # Adding model 'Role'
        db.create_table('me_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('me', ['Role'])

        # Adding model 'Participation'
        db.create_table('me_participation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['me.Project'])),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['me.Participant'])),
        ))
        db.send_create_signal('me', ['Participation'])

        # Adding M2M table for field role on 'Participation'
        db.create_table('me_participation_role', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participation', models.ForeignKey(orm['me.participation'], null=False)),
            ('role', models.ForeignKey(orm['me.role'], null=False))
        ))
        db.create_unique('me_participation_role', ['participation_id', 'role_id'])

        # Adding model 'Tweet'
        db.create_table('me_tweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=20, decimal_places=17)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=20, decimal_places=17)),
        ))
        db.send_create_signal('me', ['Tweet'])


    def backwards(self, orm):
        # Removing unique constraint on 'RoleTranslation', fields ['language_code', 'master']
        db.delete_unique('me_role_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ParticipantTranslation', fields ['language_code', 'master']
        db.delete_unique('me_participant_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ProjectTranslation', fields ['language_code', 'master']
        db.delete_unique('me_project_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ProjectTypeTranslation', fields ['language_code', 'master']
        db.delete_unique('me_projecttype_translation', ['language_code', 'master_id'])

        # Deleting model 'Social'
        db.delete_table('me_social')

        # Deleting model 'ProjectTypeTranslation'
        db.delete_table('me_projecttype_translation')

        # Deleting model 'ProjectType'
        db.delete_table('me_projecttype')

        # Deleting model 'ProjectTranslation'
        db.delete_table('me_project_translation')

        # Deleting model 'Project'
        db.delete_table('me_project')

        # Removing M2M table for field project_type on 'Project'
        db.delete_table('me_project_project_type')

        # Deleting model 'Screenshot'
        db.delete_table('me_screenshot')

        # Deleting model 'ParticipantTranslation'
        db.delete_table('me_participant_translation')

        # Deleting model 'Participant'
        db.delete_table('me_participant')

        # Deleting model 'RoleTranslation'
        db.delete_table('me_role_translation')

        # Deleting model 'Role'
        db.delete_table('me_role')

        # Deleting model 'Participation'
        db.delete_table('me_participation')

        # Removing M2M table for field role on 'Participation'
        db.delete_table('me_participation_role')

        # Deleting model 'Tweet'
        db.delete_table('me_tweet')


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
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
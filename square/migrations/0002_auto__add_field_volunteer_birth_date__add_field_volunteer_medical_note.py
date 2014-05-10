# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Volunteer.birth_date'
        db.add_column(u'square_volunteer', 'birth_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Volunteer.medical_notes'
        db.add_column(u'square_volunteer', 'medical_notes',
                      self.gf('django.db.models.fields.TextField')(max_length=400, null=True),
                      keep_default=False)

        # Adding field 'Volunteer.conduct_notes'
        db.add_column(u'square_volunteer', 'conduct_notes',
                      self.gf('django.db.models.fields.TextField')(max_length=400, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Volunteer.birth_date'
        db.delete_column(u'square_volunteer', 'birth_date')

        # Deleting field 'Volunteer.medical_notes'
        db.delete_column(u'square_volunteer', 'medical_notes')

        # Deleting field 'Volunteer.conduct_notes'
        db.delete_column(u'square_volunteer', 'conduct_notes')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'square.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 9, 0, 0)'}),
            'end': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2014, 5, 9, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_volunteer_time': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['square.EventLocation']"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'start': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2014, 5, 9, 0, 0)'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Open Build'", 'max_length': '50'})
        },
        u'square.eventlocation': {
            'Meta': {'object_name': 'EventLocation'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        u'square.session': {
            'Meta': {'object_name': 'Session'},
            'end': ('django.db.models.fields.TimeField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['square.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orientation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'volunteer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['square.Volunteer']"})
        },
        u'square.volunteer': {
            'Meta': {'object_name': 'Volunteer'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'conduct_notes': ('django.db.models.fields.TextField', [], {'max_length': '400', 'null': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'contact_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'contact_relationship': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medical_notes': ('django.db.models.fields.TextField', [], {'max_length': '400', 'null': 'True'}),
            'signup_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 9, 0, 0)'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['square']
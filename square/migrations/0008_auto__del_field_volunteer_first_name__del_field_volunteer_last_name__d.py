# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Volunteer.first_name'
        db.delete_column(u'square_volunteer', 'first_name')

        # Deleting field 'Volunteer.last_name'
        db.delete_column(u'square_volunteer', 'last_name')

        # Deleting field 'Volunteer.vol_image'
        db.delete_column(u'square_volunteer', 'vol_image')

        # Adding field 'Volunteer.full_name'
        db.add_column(u'square_volunteer', 'full_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Volunteer.email'
        db.add_column(u'square_volunteer', 'email',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Deleting field 'Event.event_type'
        db.delete_column(u'square_event', 'event_type')

        # Deleting field 'Event.event_location'
        db.delete_column(u'square_event', 'event_location_id')

        # Adding field 'Event.type'
        db.add_column(u'square_event', 'type',
                      self.gf('django.db.models.fields.CharField')(default='Open Build', max_length=50),
                      keep_default=False)

        # Adding field 'Event.date'
        db.add_column(u'square_event', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 5, 9, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.location'
        db.add_column(u'square_event', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['square.EventLocation']),
                      keep_default=False)


        # Changing field 'Event.start'
        db.alter_column(u'square_event', 'start', self.gf('django.db.models.fields.TimeField')())

        # Changing field 'Event.end'
        db.alter_column(u'square_event', 'end', self.gf('django.db.models.fields.TimeField')())

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Volunteer.first_name'
        raise RuntimeError("Cannot reverse this migration. 'Volunteer.first_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Volunteer.first_name'
        db.add_column(u'square_volunteer', 'first_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Volunteer.last_name'
        raise RuntimeError("Cannot reverse this migration. 'Volunteer.last_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Volunteer.last_name'
        db.add_column(u'square_volunteer', 'last_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)

        # Adding field 'Volunteer.vol_image'
        db.add_column(u'square_volunteer', 'vol_image',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Deleting field 'Volunteer.full_name'
        db.delete_column(u'square_volunteer', 'full_name')

        # Deleting field 'Volunteer.email'
        db.delete_column(u'square_volunteer', 'email')


        # User chose to not deal with backwards NULL issues for 'Event.event_type'
        raise RuntimeError("Cannot reverse this migration. 'Event.event_type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Event.event_type'
        db.add_column(u'square_event', 'event_type',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Event.event_location'
        raise RuntimeError("Cannot reverse this migration. 'Event.event_location' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Event.event_location'
        db.add_column(u'square_event', 'event_location',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['square.EventLocation']),
                      keep_default=False)

        # Deleting field 'Event.type'
        db.delete_column(u'square_event', 'type')

        # Deleting field 'Event.date'
        db.delete_column(u'square_event', 'date')

        # Deleting field 'Event.location'
        db.delete_column(u'square_event', 'location_id')


        # Changing field 'Event.start'
        db.alter_column(u'square_event', 'start', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Event.end'
        db.alter_column(u'square_event', 'end', self.gf('django.db.models.fields.DateTimeField')())

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
            'is_volunteer_time': ('django.db.models.fields.BooleanField', [], {}),
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
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signup_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 9, 0, 0)'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['square']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Volunteer.credentials'
        db.add_column(u'square_volunteer', 'credentials',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300, blank=True),
                      keep_default=False)

        # Adding field 'Volunteer.vol_image'
        db.add_column(u'square_volunteer', 'vol_image',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Volunteer.credit'
        db.add_column(u'square_volunteer', 'credit',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=7, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Volunteer.credentials'
        db.delete_column(u'square_volunteer', 'credentials')

        # Deleting field 'Volunteer.vol_image'
        db.delete_column(u'square_volunteer', 'vol_image')

        # Deleting field 'Volunteer.credit'
        db.delete_column(u'square_volunteer', 'credit')


    models = {
        u'square.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 20, 0, 0)'}),
            'end': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(1900, 1, 1, 0, 0)'}),
            'event_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['square.EventLocation']"}),
            'event_type': ('django.db.models.fields.CharField', [], {'default': "'VP'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_volunteer_time': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'start': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(1900, 1, 1, 0, 0)'})
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
            'credentials': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '7', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'blank': 'True'}),
            'hours': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'signup_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 20, 0, 0)'}),
            'vol_image': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['square']
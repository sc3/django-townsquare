# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Volunteer'
        db.create_table(u'square_volunteer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100, blank=True)),
            ('signup_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 8, 12, 0, 0))),
            ('hours', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'square', ['Volunteer'])

        # Adding model 'EventLocation'
        db.create_table(u'square_eventlocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal(u'square', ['EventLocation'])

        # Adding model 'Event'
        db.create_table(u'square_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_type', self.gf('django.db.models.fields.CharField')(default='VP', max_length=2)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 8, 12, 0, 0))),
            ('start', self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(1900, 1, 1, 0, 0))),
            ('end', self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(1900, 1, 1, 0, 0))),
            ('event_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['square.EventLocation'])),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_volunteer_time', self.gf('django.db.models.fields.NullBooleanField')(default=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'square', ['Event'])

        # Adding model 'Session'
        db.create_table(u'square_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('volunteer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['square.Volunteer'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['square.Event'])),
            ('start', self.gf('django.db.models.fields.TimeField')()),
            ('end', self.gf('django.db.models.fields.TimeField')()),
            ('orientation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('forgot_signout', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'square', ['Session'])


    def backwards(self, orm):
        # Deleting model 'Volunteer'
        db.delete_table(u'square_volunteer')

        # Deleting model 'EventLocation'
        db.delete_table(u'square_eventlocation')

        # Deleting model 'Event'
        db.delete_table(u'square_event')

        # Deleting model 'Session'
        db.delete_table(u'square_session')


    models = {
        u'square.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 12, 0, 0)'}),
            'end': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(1900, 1, 1, 0, 0)'}),
            'event_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['square.EventLocation']"}),
            'event_type': ('django.db.models.fields.CharField', [], {'default': "'VP'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_volunteer_time': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['square.Volunteer']", 'through': u"orm['square.Session']", 'symmetrical': 'False'}),
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
            'forgot_signout': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orientation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'volunteer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['square.Volunteer']"})
        },
        u'square.volunteer': {
            'Meta': {'object_name': 'Volunteer'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'blank': 'True'}),
            'hours': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'signup_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 12, 0, 0)'})
        }
    }

    complete_apps = ['square']
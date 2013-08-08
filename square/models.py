from django.db import models
from utils import timedelta
from datetime import datetime

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    signup_date = models.DateField(default=datetime.now())
    hours = models.FloatField(editable=False, default=None)    

    def calculate_hours(self):
        return sum(
	    [round(timedelta(s.end, s.start).seconds / 3600.0, 1) 
	    for s in self.session_set.filter() 
	    if s.event.volunteer_time])

    def save(self, *args, **kwargs):
	# doesn't work; have to reload volunteer to see correct hours
	# consider using signals...
        self.hours = self.calculate_hours()
        super(Volunteer, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class EventLocation(models.Model):
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)

    def __unicode__(self):
        return self.full_name

class Event(models.Model):
    EVENT_TYPES = {
        ('VP', 'Volunteer Program'),
        ('CL', 'Class'),
        ('WS', 'Workshop'),
        ('PR', 'Presentation'),
        ('CM', 'Community Meeting'),
        ('VM', 'Vision Meeting'),
        ('FR', 'Fundraiser'),
        ('SP', 'Special Event')
    }

    event_type = models.CharField(max_length=2, choices=EVENT_TYPES, default='VP')
    date = models.DateField(default=datetime.now())
    start = models.TimeField(default=datetime.strptime('11:00AM', '%I:%M%p'))
    end = models.TimeField(default=datetime.strptime('5:00PM', '%I:%M%p'))
    event_location = models.ForeignKey(EventLocation)
    notes = models.TextField(blank=True)
    volunteer_time = models.NullBooleanField(default=None)

    def save(self, *args, **kwargs):
        if self.volunteer_time is None:
            self.volunteer_time = self.counts_towards_volunteer_time()
        super(Event, self).save(*args, **kwargs)

    def counts_towards_volunteer_time(self):
        return self.event_type == 'VP'

    def __unicode__(self):
	for abbrev, longform in self.EVENT_TYPES:
            if abbrev == self.event_type:
                long_type = longform
        return "%s on %s" % (long_type, self.date)

class Session(models.Model):
    ROLES = {
        ('PT', 'Participant'),
        ('ST', 'Staff'),
    }
    volunteer = models.ForeignKey(Volunteer)
    role = models.CharField(max_length=100, choices=ROLES, default='PT')
    event = models.ForeignKey(Event)
    start = models.TimeField()
    end = models.TimeField()
    orientation = models.BooleanField(default=False)
    forgot_signout = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s at %s" % (self.volunteer, self.event)

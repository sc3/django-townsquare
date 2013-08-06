from django.db import models
from utils import timedelta

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    signup_date = models.DateField()    

    def calculate_hours(self):
        hours = 0
        for s in self.session_set.all():
            tdelta = timedelta(s.end, s.start)
            hour_diff = tdelta.seconds / 3600.00
	    hours += hour_diff
	return hours

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
    type = models.CharField(max_length=2, choices=EVENT_TYPES, default='VP')
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    event_location = models.ForeignKey(EventLocation)
    notes = models.TextField(blank=True)

    def __unicode__(self):
	for abbrev, longform in self.EVENT_TYPES:
            if abbrev == self.type:
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

    def __unicode__(self):
        return "%s at %s" % (self.volunteer, self.event)

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Volunteer(models.Model):
    user = models.OneToOneField(User, null=True)
    signup_date = models.DateField("Sign-up date", default=datetime.now())
    hours = models.FloatField(editable=False, default=0.0) 
    credentials = models.CharField(max_length=300, blank=True)
    vol_image = models.CharField(max_length=200, blank=True)
    credit = models.FloatField(editable=False, default=0.0)   

    def full_name(self):
        return self.user.first_name + " " + self.user.last_name

    def calculate_hours(self):
        hours = 0
        for s in self.session_set.all():
            if s.event.is_volunteer_time:
                tdelta = timeonly_delta(s.end, s.start)
                hour_diff = tdelta.seconds / 3600.0
                rounded = round(hour_diff, 1)
                hours += rounded
        return hours

    def save(self, *args, **kwargs):
        self.hours = self.calculate_hours()
        self.credit += self.hours
        super(Volunteer, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name

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
        ('ME', 'Meeting'),
        ('SP', 'Special Event')
    }

    event_type = models.CharField(max_length=2, choices=EVENT_TYPES, default='VP')
    date = models.DateField(default=datetime.now())
    start = models.TimeField(default=datetime.strptime('11:00AM', '%I:%M%p'))
    end = models.TimeField(default=datetime.strptime('5:00PM', '%I:%M%p'))
    event_location = models.ForeignKey(EventLocation)
    notes = models.TextField(blank=True)
    is_volunteer_time = models.BooleanField('Counts towards volunteer hours')

    def __unicode__(self):
	for abbrev, longform in self.EVENT_TYPES:
            if abbrev == self.event_type:
                long_type = longform
        return "%s on %s" % (long_type, self.date)

class Session(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    event = models.ForeignKey(Event)
    start = models.TimeField()
    end = models.TimeField()
    orientation = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Session, self).save(*args, **kwargs)
        self.volunteer.save()

    def __unicode__(self):
        return "%s at %s" % (self.volunteer, self.event)


from utils import timeonly_delta

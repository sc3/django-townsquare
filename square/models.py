
from django.db import models
from django.contrib.auth.models import User
from square.utils import timeonly_delta
from datetime import datetime


class Volunteer(models.Model):

    PERMISSION_GROUPS = {
        ('Staff', 'Staff'),
        ('Admin', 'Admin'),
        ('Volunteer', 'Volunteer')
    }
        
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, unique=True, null=True)
    signup_date = models.DateField("Sign-up date", default=datetime.now())
    hours = models.FloatField(editable=False, default=0.0, max_length=20) 
    credentials = models.CharField(max_length=200, null=True, blank=True)
    vol_image = models.CharField(max_length=200, blank=True)
    credit = models.IntegerField(editable=False, default=0, max_length=20)

    def add_session(self, s):
        if s.event.is_volunteer_time:
            tdelta = timeonly_delta(s.end, s.start)
            hour_diff = tdelta.seconds / 3600.0
            rounded = round(hour_diff, 1)
            self.hours += rounded
            self.calculate_credit(rounded)

    def calculate_credit(self, hours):
        self.credit += (hours * 100)

    def _get_full_name(self):
        return self.first_name + " " + self.last_name

    def _get_last_seen(self):
        try:
            s = self.session_set.latest('event__date')
            return s.event.date
        except StandardError:
            return None

    def _get_permission(self):
    	return self.user.groups.filter()[0].name

    full_name = property(_get_full_name)
    last_seen = property(_get_last_seen)
    permission = property(_get_permission)

    def __unicode__(self):
        return self.full_name


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

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
        for s in self.session_set.all():
            s.save()


class Session(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    event = models.ForeignKey(Event)
    start = models.TimeField()
    end = models.TimeField()
    orientation = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Session, self).save(*args, **kwargs)
        self.volunteer.add_session(self)
        self.volunteer.save()

    def __unicode__(self):
        return "%s at %s" % (self.volunteer, self.event)

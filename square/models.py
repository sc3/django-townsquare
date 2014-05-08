
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
    vol_image = models.CharField(max_length=200, blank=True)

    @property
    def hours(self):
        hours = 0.0
        for s in self.session_set.filter(event__is_volunteer_time=True):
            hours += s.elapsed_time
        
        return hours

    @property
    def rewards_used(self):
        pass
        # rewards_used = 0
        # for s in self.sale_set:
        #     if s.uses_rewards:
        #         rewards_used += s.amount

    @property
    def credit(self):
        return self.hours
        # return (self.hours - self.rewards_used) 

    @ property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def last_seen(self):
        try:
            s = self.session_set.latest('event__date')
            return s.event.date
        except StandardError:
            return None

    @property
    def permission(self):
        # take the first permission group a volunteer is in;
        # they should only be in one 
    	return self.user.groups.filter()[0].name

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


class Session(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    event = models.ForeignKey(Event)
    start = models.TimeField()
    end = models.TimeField()
    orientation = models.BooleanField(default=False)

    @property
    def elapsed_time(self):
        tdelta = timeonly_delta(self.end, self.start)
        hour_diff = tdelta.seconds / 3600.0
        return round(hour_diff, 1)

    def __unicode__(self):
        return "%s at %s" % (self.volunteer, self.event)


# class Sale(models.Model):
#     uses_rewards = models.BooleanField(default=False)
#     # price in cents
#     total_price = models.IntegerField(default=0)
#     staff = models.ForeignKey(Volunteer)
#     description = models.TextField()




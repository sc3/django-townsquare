
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
        
    full_name = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, unique=True, null=True)
    signup_date = models.DateField("Date of Orientation", default=datetime.today())

    @property
    def hours(self):
        hours = 0.0
        for s in self.session_set.filter(event__is_volunteer_time=True):
            hours += s.elapsed_time
        
        return hours

    @property
    def rewards_used(self):
        rewards_used = 0.0
        # for s in self.sale_set.all():
        #     if s.uses_rewards:
        #         rewards_used += s.amount
        return rewards_used

    @property
    def credit(self):
        return (self.hours - self.rewards_used) 

    @property
    def last_seen(self):
        try:
            s = self.session_set.latest('event__start')
            return s.event.date
        except StandardError:
            return None

    @property
    def permission(self):
        # take the first permission group a volunteer is in;
        # they should be in exactly one group 
        try:
            return self.user.groups.filter()[0].name
        except IndexError:
            return None


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

#
# after EventLocation to avoid recursive import; before Event
# so that it can be used there
# from square.management.commands.initialize import initial_event_location
#
#

class Event(models.Model):
    EVENT_TYPES = {
        ('Open Build', 'Open Build'),
        ('Community Council', 'Community Council'),
        ('Special Event', 'Special Event')
    }

    type = models.CharField(max_length=50, choices=EVENT_TYPES, default='Open Build')
    date = models.DateField(default=datetime.today())
    start = models.TimeField(default=datetime.now())
    end = models.TimeField(default=datetime.now())
    location = models.ForeignKey(EventLocation, default=EventLocation(id=1))
    notes = models.TextField(blank=True)
    is_volunteer_time = models.BooleanField('Counts towards volunteer hours', default=True)

    @property
    def total_participants(self):
        return self.session_set.count()

    @property
    def total_service_hours(self):
        hours = 0
        for s in self.session_set.all():
            hours += s.elapsed_time
        return hours

    def __str__(self):
        return "{0} on {1}".format(self.type, self.date)


class Session(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    event = models.ForeignKey(Event)
    start = models.TimeField('Time In')
    end = models.TimeField('Time Out')
    orientation = models.BooleanField(default=False)

    @property
    def elapsed_time(self):
        tdelta = timeonly_delta(self.end, self.start)
        return round(tdelta, 1)

    def __unicode__(self):
        return "{0} at {1}".format(self.volunteer, self.event)


# class Sale(models.Model):
#     uses_rewards = models.BooleanField(default=False)
#     # price in cents
#     total_price = models.IntegerField(default=0)
#     staff = models.ForeignKey(Volunteer)
#     description = models.TextField()

from django.db import models
from django.contrib.auth.models import User

from townsquare.utils import timeonly_delta

from datetime import datetime, time


class Volunteer(models.Model):

    """ Volunteer model. Handles volunteer contact 
        information, interfaces with Session model for 
        recording volunteer participation in an Event, 
        manages user permission for staff & volunteer 
        login, and has several methods for lazily 
        evalulating hours served, store credit available,
        last seen date, and permission level. """

    STAFF = 'S'
    ADMIN = 'A'
    VOLUNTEER = 'V'
    PERMISSION_GROUPS = {
        (STAFF, 'Staff'),
        (ADMIN, 'Admin'),
        (VOLUNTEER, 'Volunteer')
    }
        
    full_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    user = models.OneToOneField(User, unique=True, null=True)
    signup_date = models.DateField("Date of Orientation", 
            default=datetime.today())
    legal_date = models.DateField(
            "Date Signed Waiver and Code of Conduct", 
            null=True, blank=True, default=datetime.today())
    birth_date = models.DateField(null=True, blank=True)
    contact_name = models.CharField(max_length=200, blank=True)
    contact_relationship = models.CharField(max_length=200,
            blank=True)
    contact_phone_number = models.CharField(max_length=200,
            blank=True)
    medical_notes = models.TextField(max_length=400, 
            blank=True)
    conduct_notes = models.TextField("Code of Conduct Notes",
            max_length=400, blank=True)

    @property
    def hours(self):
        """ Hours are calculated based on all sessions 
            from events with is_volunteer_time set to True. """
        hours = 0.0
        for s in self.session_set.filter(
                event__is_volunteer_time=True):
            hours += s.elapsed_time
        return hours

    @property
    def rewards_used(self):
        """ Amount of rewards used is not yet implemented, 
            because the Sale model can't be meaningfully
            implemented yet. """
        rewards_used = 0.0
        # for s in self.sale_set.all():
        #     if s.uses_rewards:
        #         rewards_used += s.total_price
        return rewards_used

    @property
    def credit(self):
        """ Total credit available is equal to total 
            hours worked minus total rewards used"""
        return (self.hours - self.rewards_used) 

    @property
    def last_seen(self):
        try:
            s = self.session_set.latest('event__date')
            return s.event.date
        except StandardError:
            return None

    @property
    def permission(self):
        """ Take the first permission group a volunteer is in;
            they should be in exactly one group. """
        try:
            return self.user.groups.filter()[0].name
        except IndexError:
            return None

    def __str__(self):
        return self.full_name


class EventLocation(models.Model):

    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)
    def __str__(self):
        return self.full_name


def initial_event_location():

    try:
        return EventLocation.objects.get(id=1)
    except EventLocation.DoesNotExist:
        el = EventLocation.objects.create(
            full_name='FreeGeek Chicago', 
            address='3411 W. Diversey Avenue',
            city='Chicago',
            state='IL',
            zip_code='60647'
        )
        el.save()
        return el


class Event(models.Model):

    """ Event model. This handles the date and time of 
        events which Volunteers register with through the 
        Session model. It defines a few convenience 
        properties for calculating the total number of
        participants and total number of service hours.  """

    OPEN_BUILD = 'OB'
    OPEN_HACK = 'OH'
    COMMUNITY_COUNCIL = 'CC'
    VISION_MEETING = 'VM'
    SPECIAL_EVENT = 'SE'
    EVENT_TYPES = {
        (OPEN_BUILD, 'Open Build'),
        (OPEN_HACK, 'Open Hack'),
        (COMMUNITY_COUNCIL, 'Community Council'),
        (VISION_MEETING, 'Vision Meeting'),
        (SPECIAL_EVENT, 'Special Event')
    }

    type = models.CharField(max_length=50, 
            choices=EVENT_TYPES, default=OPEN_BUILD)
    date = models.DateField(default=datetime.today())
    start = models.TimeField(default=time(11))
    end = models.TimeField(default=time(11))
    location = models.ForeignKey(EventLocation, 
            default=initial_event_location()) 
    notes = models.TextField(blank=True)
    is_volunteer_time = models.BooleanField(
            'Counts towards volunteer hours', 
            default=True)

    @property
    def total_participants(self):
        """ For the moment, on the assumption that a 
            volunteer can only participate once in 
            an event, number of participants is 
            equivalent to number of sessions,
            for that event. """
        return self.session_set.count()

    @property
    def total_service_hours(self):
        hours = 0.0
        for s in self.session_set.filter(
                    event__is_volunteer_time=True):
            hours += s.elapsed_time
        return hours

    def __str__(self):
        return "{0} on {1}".format(self.get_type_display(), self.date)


class Session(models.Model):

    """ Session model that represents a unique association
        between Volunteer, Event, and start and end times. 
        Defines a convenience property for calculating 
        the elapsed time of a Session. """

    volunteer = models.ForeignKey(Volunteer)
    event = models.ForeignKey(Event)
    start = models.TimeField('Time In')
    end = models.TimeField('Time Out')
    orientation = models.BooleanField(default=False)

    @property
    def elapsed_time(self):
        tdelta = timeonly_delta(self.end, self.start)
        return round(tdelta, 1)

    def __str__(self):
        return "{0} at {1}".format(self.volunteer, self.event)

from datetime import date, time, datetime
from django.contrib.auth.models import User
from square.models import Volunteer, Event, EventLocation

from django.core import serializers

def timeonly_delta(time1, time2):
    start_date = dateize(time1)
    end_date = dateize(time2)
    return start_date-end_date


def dateize(time):
    return datetime.combine(date.today(), time)


def process_user(uname, pw, first, last):

	u = User.objects.create_user(
		first_name=first, 
		last_name=last, 
		password=pw, 
		username=uname)

	u.save()

	v = Volunteer(user=u)
	
	v.save()

	return v

	
#evt=event time, evl=event location, d=date, start=start time, end=end time, notes=notes, vt=is_volunteer_time
def process_event(evt, evl, d, start, end, notes, vt):
	
	e = Event(
	event_type=evt,
	event_location=EventLocation(evl),
	date=d,
	start=start,
	end=end,
	notes=notes,
	is_volunteer_time=vt)
	
	e.save()
	
	return(e)
		
		

from datetime import date, time, datetime
from django.contrib.auth.models import User
from square.models import Volunteer

def timeonly_delta(time1, time2):
    start_date = dateize(time1)
    end_date = dateize(time2)
    return start_date-end_date

def dateize(time):
    return datetime.combine(date.today(), time)

def process_user(uname, pw, first, last):
	u = User(first_name=first, last_name=last, password=pw, username=uname)
	u.save()
	v = Volunteer(user=u, signup_date=datetime.today())
	v.save()
	return v

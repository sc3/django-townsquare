from square.models import Volunteer, Event, EventLocation
from square.utils import gen_password, gen_username
from square.forms import VolunteerForm, LoginForm, EventForm
from django.contrib.auth.models import User
from datetime import datetime

def process_valid_login_post(request, form):

    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    
    user = authenticate(username=username, password=password)           
    if (user is not None) and user.is_active:
    
        login(request, user)
        return True
    
    else:
        return False


def process_valid_volunteer_post(form):

    uname = form.cleaned_data['username']
    pw = form.cleaned_data['password']
    first = form.cleaned_data['first_name']
    last = form.cleaned_data['last_name']

    if not uname:
        # if a username is not provided, make one from 
        # first name, last name, and sign up date
        uname = gen_username(first, last, datetime.now())

    # associate a django user object with this volunteer
    try:
        u = User.objects.get(username=uname)
    except User.DoesNotExist:
        u = User.objects.create_user(
            first_name=first, 
            last_name=last, 
            password=pw, 
            username=uname)
        u.save()

    try:
        v = Volunteer.objects.get(user=u)
        # do some more updating on vol
    except Volunteer.DoesNotExist:
        # prepare some more values to update vol
        v = Volunteer(user=u)

    # create or update this volunteer
    v.save()

    
def process_volunteer_get(vol_id):

    if vol_id is None:
        raise Exception("Can't POST to this URL. Try editing a specific "
                        "volunteer: append '/n', where n is the id of the "
                        "volunteer you want.")

    vol = Volunteer.objects.get(id=int(vol_id))
    vol_fields = {  
            'first_name': vol.user.first_name, 
            'last_name': vol.user.last_name,
            'username': vol.user.username,
            'password': vol.user.password
    }
    return VolunteerForm(initial=vol_fields)    


def process_valid_event_post(form):

    update_fields = {}
    for k in form.fields:
        if form.cleaned_data[k]:
            update_fields[k] = form.cleaned_data[k]

    result = Event.objects.update(**update_fields)
    if result == 0:
        e = Event(**update_fields)
        e.save()


def process_event_get(event_id):

    if event_id is None:
        raise Exception("Can't POST to this URL. Try editing a specific "
                        "event: append '/n', where n is the id of the event "
                        "you want .")

    event = Event.objects.get(id=int(event_id))
    return EventForm(instance=event)


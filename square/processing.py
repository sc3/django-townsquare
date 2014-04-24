from square.models import Volunteer, Event, EventLocation
from square.utils import gen_password, gen_username
from square.forms import VolunteerForm, LoginForm, EventForm
from django.contrib.auth import authenticate, login
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


    # define a few sets of args to initialize or update user
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']


    # set user permissions based on volunteer credentials
    permissions = {
        'ST' : 'is_superuser',
        'AD' : 'is_staff',
        'VO' : ''
    }
    p = form.cleaned_data['credentials']
    # TODO: add proper permissions to user model

    # if a username is not provided, make one from 
    # first name, last name, and sign up date
    first_name = form.cleaned_data['first_name']
    last_name = form.cleaned_data['last_name']
    if not username:
        username = gen_username(first_name, last_name, datetime.now())


    # update or create a user object
    u_q = User.objects.filter(username=username)
    if u_q.count():
        u = u_q[0]
        _ = u_q.update(username=username, 
                        password=password)
    else:
        u = User.objects.create_user(username, password)
        u.save()


    # define a set of volunteer fields, and get them from the form
    vol_fieldnames = ['first_name', 'last_name', 'credentials']
    vol_fields = {k: form.cleaned_data[k] for k in form.fields if k and k in vol_fieldnames}
    
    # add the user we created to the volunteer fields
    vol_fields['user'] = u


    # update or create the volunteer
    v_q = Volunteer.objects.filter(user=u)
    if v_q.count():
        _  = v_q.update(**vol_fields)
        v = v_q[0]
    else:
        v = Volunteer.objects.create(**vol_fields)

    v.save()

    
def process_volunteer_get(vol_id):

    if vol_id is None:
        raise Exception("Can't POST to this URL. Try editing a specific "
                        "volunteer: append '/n', where n is the id of the "
                        "volunteer you want.")

    vol = Volunteer.objects.get(id=int(vol_id))
    vol_fields = {  
            'first_name': vol.first_name, 
            'last_name': vol.last_name,
            'username': vol.user.username,
            'password': vol.user.password,
            'credentials': vol.credentials
    }
    return VolunteerForm(initial=vol_fields) 


def process_valid_event_post(form):

    update_fields = {}
    for k in form.fields:
        if form.cleaned_data[k]:
            update_fields[k] = form.cleaned_data[k]

    result = Event.objects.update(**update_fields)
    if not result:
        e = Event(**update_fields)
        e.save()


def process_event_get(event_id):

    if event_id is None:
        raise Exception("Can't POST to this URL. Try editing a specific "
                        "event: append '/n', where n is the id of the event "
                        "you want .")

    event = Event.objects.get(id=int(event_id))
    return EventForm(instance=event)


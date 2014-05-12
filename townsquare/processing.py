from townsquare.models import Volunteer, Event, EventLocation
from townsquare.utils import gen_password, gen_username
from townsquare.forms import VolunteerForm, LoginForm, EventForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
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


def process_valid_volunteer_post(form, vol_id=None):

    new_username = form.cleaned_data['username']
    new_password = form.cleaned_data['password']


    # if a username is not provided, make one from 
    # first name, last name, and sign up date
    new_full_name = form.cleaned_data['full_name']
    if not new_username:
        new_username = gen_username(new_full_name, datetime.now())


    # find out whether new username is being used
    try:
        user = User.objects.get(username=new_username)

        # if it is, make sure it's by volunteer we're editing 
        if user.volunteer.id == vol_id:

            # update user fields if supplied
            if new_username:
                user.username = new_username
            if new_password:
                user.password = new_password

    # new username hasn't been taken
    except User.DoesNotExist:

        try:
            # try to get the volunteer we're editing
            vol = Volunteer.objects.get(id=vol_id)

            # if it exists, get that volunteer's associated user
            user = vol.user

            # update the username and password of the user
            # with the new fields
            user.username = new_username
            user.password = new_password

        # if there is no volunteer yet, just create the new user
        except Volunteer.DoesNotExist:

            user = User.objects.create_user(new_username, password=new_password)


    # add volunteer permission to user
    new_permission = form.cleaned_data['permission']
    try:
        new_group = Group.objects.get(name=new_permission)
    except Group.DoesNotExist:
        raise Exception("Invalid permission level: '{0}'".format(new_permission))
    user.groups.add(new_group)
    user.save()


    # define a set of volunteer fields, and get them from the form
    vol_fieldnames = ['full_name']
    vol_fields = {k: form.cleaned_data[k] for k in form.fields if k and k in vol_fieldnames}
    
    # add the user we updated/created to the volunteer fields
    vol_fields['user'] = user

    # update/create the volunteer
    try:
        vol = Volunteer.objects.get(user=user)
        vol.__dict__.update(**vol_fields)
    except Volunteer.DoesNotExist:
        vol = Volunteer.objects.create(**vol_fields)

    vol.save()

    
def process_volunteer_get(vol_id):

    vol = Volunteer.objects.get(id=int(vol_id))
    vol_fields = {  
            'full_name': vol.full_name,
            'username': vol.user.username,
            'password': vol.user.password,
            'permission': vol.permission
    }
    return VolunteerForm(initial=vol_fields) 


def process_valid_event_post(form, event_id=None):

    # TODO: Fix this! Does this code never result
    # in more than one event being created?

    update_fields = {}
    for k in form.fields:
        if form.cleaned_data[k]:
            update_fields[k] = form.cleaned_data[k]

    result = Event.objects.update(**update_fields)
    if not result:
        e = Event(**update_fields)
        e.save()


def process_event_get(event_id):

    if event_id is not None:
        event = Event.objects.get(id=int(event_id))
        return EventForm(instance=event)
        



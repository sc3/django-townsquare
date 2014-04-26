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


def process_valid_volunteer_post(request, form):


    vol_id = int(request.session['vol_id'])

    new_username = form.cleaned_data['username']
    new_password = form.cleaned_data['password']

    # set user permissions based on volunteer credentials
    # permissions = {
    #     'ST' : 'is_superuser',
    #     'AD' : 'is_staff',
    #     'VO' : ''
    # }
    # new_permissions = form.cleaned_data['credentials']
    # TODO: add proper permissions to user model


    # if a username is not provided, make one from 
    # first name, last name, and sign up date
    new_firstname = form.cleaned_data['first_name']
    new_lastname = form.cleaned_data['last_name']
    if not new_username:
        new_username = gen_username(new_firstname, new_lastname, datetime.now())

    # import pdb; pdb.set_trace(); 

    # find out whether username is already being used
    user_queryset = User.objects.filter(username=new_username)

    # username is already taken
    if user_queryset.count():
        old_user = user_queryset[0]

        # user with this username is the same one we're editing 
        if old_user.volunteer.id == vol_id:
            _ = user_queryset.update(username=new_username, 
                                     password=new_password)
            user = old_user

        else:
            # can't change username to that of an existing user
            pass


    # username not taken
    else:
        # get the volunteer we're trying to edit
        vol_queryset = Volunteer.objects.filter(id=vol_id)

        # if it exists, get that volunteer's associated user
        if vol_queryset.count():
            old_user = vol_queryset[0].user
            

            # update the username and password of the user we're editing
            old_user.username = new_username
            old_user.password = new_password

            user = old_user
        else:
            # if not, create the new user
            new_user = User.objects.create_user(new_username, new_password)
            user = new_user

    user.save()


    # define a set of volunteer fields, and get them from the form
    vol_fieldnames = ['first_name', 'last_name', 'credentials']
    vol_fields = {k: form.cleaned_data[k] for k in form.fields if k and k in vol_fieldnames}
    
    # add the user we created to the volunteer fields
    vol_fields['user'] = user


    # update or create the volunteer
    vol_queryset = Volunteer.objects.filter(user=user)
    if vol_queryset.count():
        _  = vol_queryset.update(**vol_fields)
        vol = vol_queryset[0]
    else:
        vol = Volunteer.objects.create(**vol_fields)

    vol.save()

    
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


def process_valid_event_post(form, vol_id=None):

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


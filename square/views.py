from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from square.models import Volunteer, Event
from square.forms import VolunteerForm, LoginForm, EventForm
from square.processing import process_volunteer, process_volunteer


def about(request):
    
    blurb = "Something about Townsquare."
    return render(request, 'users/about.html', 
                    {'blurb': blurb,})


def t2login(request):
    
    if request.method == 'POST':
        
        # POST request to login page does validation/processing
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        
            user = authenticate(username=username, password=password)
            
            
            if user is not None:
            
                if user.is_active:
                    
                    login(request, user)
                    return HttpResponseRedirect('/townsquare/volunteer/home')
                    
                else:

                    # this user is not allowed to access their account
                    return HttpResponseRedirect('/townsquare/login')
            
            else:
            
                return HttpResponseRedirect('/townsquare/login')
                
    
    return render(request, 'users/login.html', 
                    {'f': LoginForm()})


@login_required
def t2logout(request):
    
    logout(request)
    return HttpResponseRedirect('/townsquare/login')


@login_required 
def home(request):
    
    #Assign the information on a single volunteer as an admin
    # NOTE: catch ObjectDoesNotExist exception here, as it may occur.
    va = Volunteer.objects.get(id=request.user.volunteer.id)
    
    return render(request, 'users/index.html',
                    {'va': va})


@login_required
def add_volunteer(request):
    if request.method == 'POST':
        
        # POST request to add_volunteer page does validation/processing
        form = VolunteerForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            process_volunteer(first, last, username, password)

            return HttpResponseRedirect('/townsquare/volunteer/browse')

    else:
        # GET request to add_volunteer page displays an empty form
        form = VolunteerForm()

    return render(request, 'users/add_volunteer.html', 
                    {'f': form})


@login_required
def edit_volunteer(request, vol_id=None):

    if request.method == 'POST':

        form = VolunteerForm(request.POST)

        if form.is_valid():

            # POST request to add_volunteer page does validation/processing
            form = VolunteerForm(request.POST)

            if form.is_valid():

                uname = form.cleaned_data['username']
                pw = form.cleaned_data['password']
                first = form.cleaned_data['first_name']
                last = form.cleaned_data['last_name']
                new_user = process_volunteer(first, last, uname, pw)

            # after a successful save, go to browse events
            return HttpResponseRedirect('/townsquare/volunteer/browse')

    else:

        vol = Volunteer.objects.get(id=int(vol_id))
        form = VolunteerForm(instance=vol)
        return render(request, 'users/edit_volunteer.html',
                        {'f': form})

    # render an HTTP response if it was a GET, or an invalid POST
    return render(request, 'users/edit_volunteer.html', 
                    {'f': form})


@login_required
def browse_volunteers(request):
    
    vols = Volunteer.objects.all()
    return render(request, 'users/browse_volunteers.html',
                    {'volunteers': vols,})
    
        
@login_required
def add_event(request):

    # POST request does processing
    if request.method == 'POST':

        form = EventForm(request.POST)

        if form.is_valid():

            evt = form.cleaned_data['event_type']
            evl = form.cleaned_data['event_location']
            d = form.cleaned_data['date']
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']
            n = form.cleaned_data['notes']
            ivt = form.cleaned_data['is_volunteer_time']
            process_event(evt, evl, d, start, end, n, ivt)

            return HttpResponseRedirect('/townsquare/event/browse')

    else:
        # GET request sends an empty form
        form = EventForm()

    # render an HTTP response if it was a GET, or an invalid POST
    return render(request, 'users/add_event.html', 
                    {'f': form})


@login_required
def edit_event(request, event_id=None):

    if request.method == 'POST':

        form = EventForm(request.POST)

        if form.is_valid():

            evt = form.cleaned_data['event_type']
            evl = form.cleaned_data['event_location']
            d = form.cleaned_data['date']
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']
            n = form.cleaned_data['notes']
            ivt = form.cleaned_data['is_volunteer_time']
            process_event(evt, evl, d, start, end, n, ivt)

            # after a successful save, go to browse events
            return HttpResponseRedirect('/townsquare/event/browse')

    else:

        event = Event.objects.get(id=int(event_id))
        form = EventForm(instance=event)
        return render(request, 'users/edit_event.html',
                        {'f': form})

    # render an HTTP response if it was a GET, or an invalid POST
    return render(request, 'users/edit_event.html', 
                    {'f': form})


@login_required
def browse_events(request):
    
    evs = Event.objects.all()
    return render(request, 'users/browse_events.html',
                    {'events': evs,})
    
    


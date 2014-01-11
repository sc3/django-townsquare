from django.http import HttpResponse, HttpResponseRedirect
from square.models import Volunteer, Event, EventLocation
from django.template import Context, Template, loader, RequestContext
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from square.t2forms import SignupForm, LoginForm, AddEventForm
from square.utils import process_user, process_event


def about(request):
	
	blurb = "Something about Townsquare."
	
	t = loader.get_template('users/about.html')
	c = RequestContext(request, {'blurb':blurb,})
	
	r = t.render(c)
	
	return HttpResponse(r)


@login_required
def signup(request):
	if request.method == 'POST':
		
		# POST request to signup page does validation/processing
		form = SignupForm(request.POST)

		if form.is_valid():

			username = form.cleaned_data['Username']
			password = form.cleaned_data['Password']
			first = form.cleaned_data['first']
			last = form.cleaned_data['last']
			new_user = process_user(username, password, first, last)

			# hold onto that new user we just created, to 
			# display it in the success page.
			request.session['new_user'] = new_user.id

			return HttpResponseRedirect('/townsquare/signup-success')

	else:
		# GET request to signup page displays an empty form
		form = SignupForm()

	return render(request, 'users/signup.html', 
					{'f': form})


def t2signup_success(request):

	v = Volunteer.objects.get(id=request.session['new_user'])
	return render(request, 'users/signup-display.html', 
					{'new_user': v})


@login_required
def browse_volunteers(request):
	
	vols = Volunteer.objects.all()
	
	t = loader.get_template('users/volunteer_browse.html')
	c = RequestContext(request, {'volunteers':vols,})
	
	r = t.render(c)
	
	return HttpResponse(r)



@login_required
def search_volunteers(request):
	
	
	
	return HttpResponse()



def t2login(request):
	
	if request.method == 'POST':
		
		# POST request to login page does validation/processing
		form = LoginForm(request.POST)
		
		if form.is_valid():
			
			username = form.cleaned_data['Username']
			password = form.cleaned_data['Password']
		
			user = authenticate(username=username, password=password)
			
			
			if user is not None:
			
				if user.is_active:
					
					login(request, user)
					#Redirect to success page
					
					state="Logged in"
					
					#return HttpResponse(views.home)
					return HttpResponseRedirect('/townsquare/volunteer/home')
					
				else:
					
					return HttpResponse("Not valid")
					#Redirect to signup
			
			
			else:
			
				return HttpResponse("Sign Up")
				#Redirect to signup
			
			
				
	
	return render(request, 'users/login.html', 
					{'f': LoginForm()})
	

	
		
@login_required
def add_event(request):
	
	return render(request, 'users/add-event.html', 
					{'f': AddEventForm()})


@login_required
def t2addevent(request):
	
	""" Takes information from the addevent form and dumps
		it into the database """
	
	if request.method == 'POST':
		
		evt = request.POST['event_type']
		evl = request.POST['event_location']
		d = request.POST['date']
		start = request.POST['start']
		end = request.POST['end']
		n = request.POST['notes']
		ivt = True if request.POST.get('is_volunteer_time', None) else False
		
		new_event = process_event(evt, evl, d, start, end, n, ivt)
	
		return render(request, 'users/display-event.html', 
						{'new_event': new_event})


@login_required
def browse_events(request):
	
	evs = Event.objects.all()
	
	t = loader.get_template('users/event_browse.html')
	c = RequestContext(request, {'events':evs,})
	
	r = t.render(c)
	
	return HttpResponse(r)




		
	
def t2logout(request):
	
	logout(request)
	return HttpResponse("Logged out")


@login_required	
def home(request):
	
	#Assign the information on a single volunteer as an admin
	# NOTE: catch ObjectDoesNotExist exception here, as it may occur.
	va = Volunteer.objects.get(id=request.user.volunteer.id)
	
	return render(request, 'users/index.html',
					{'va': va})

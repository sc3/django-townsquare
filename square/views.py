from django.http import HttpResponse, HttpResponseRedirect
from square.models import Volunteer
from django.template import Context, Template, loader, RequestContext
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from square.t2forms import SignupForm, LoginForm, AddEventForm
from square.utils import process_user, process_event


def about(request):
	output = "About the Townsquare project:"
	return HttpResponse(output)


@login_required
def t2signup(request):
	if request.user.is_staff:

		return render(request, request, 'users/signup.html', 
						{'f': SignupForm()})

	else:	

		return HttpResponse("Failure")


def t2signup2(request):	

	if request.method == 'POST':
	
		username = request.POST['Username']
		password = request.POST['Password']
		first = request.POST['first']
		last = request.POST['last']
		new_user=process_user(username, password, first, last)
		
		return render(request, 'users/signup-display.html', 
						{'new_user':new_user})


def t2login(request):
	
	return render(request, 'users/login.html', 
					{'f': LoginForm()})
	

def t2login2(request):
	
	if request.method == 'POST':
	
		username = request.POST['Username']
		password = request.POST['Password']
		
		user = authenticate(username=username, password=password)
		
		if user is not None:
			
			if user.is_active:
				
				login(request, user)
				#Redirect to success page
				
				state="Logged in"
				
				#return HttpResponse(views.home)
				return HttpResponseRedirect('/townsquare/volunteers/home')
				
			else:
				
				return HttpResponse("Not valid")
				#Redirect to signup
				
		else:
			
			return HttpResponse("Sign Up")
			#Redirect to signup
	
		
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
		
	
	


def t2logout(request):
	
	logout(request)
	return HttpResponse("Logged out")




@login_required	
def home(request):
	
	#Assign the information on a single volunteer as an admin
	# NOTE: catch ObjectDoesNotExist exception here, as it may occur.
	va = Volunteer.objects.get(id=request.user.volunteer.id)
	
	#Loading template in "t" and assigning variable to context in "c"
	t = loader.get_template('users/index.html')
	c = RequestContext(request, {'va':va,})
	
	#Compiling template and rendering out the context information
	r = t.render(request, c)
	
	return HttpResponse(r)

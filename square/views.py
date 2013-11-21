from django.http import HttpResponse, HttpResponseRedirect
from square.models import Volunteer
from django.template import Context, Template, loader, RequestContext
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from square.t2forms import SignupForm, LoginForm, AddEventForm
from square.utils import process_user



def about(request):
	
	output = "About the Townsquare project:"
	return HttpResponse(output)

@login_required
def t2signup(request):
	
	if request.user.is_staff:
	
		f = SignupForm()
		
		t = loader.get_template('users/signup.html')
		c = RequestContext(request, {'f':f})
		
		r = t.render(c)
		
		return HttpResponse(r)
		
		
	else:
		
		return HttpResponse("Failure")


def t2signup2(request):	

	if request.method == 'POST':
	
		username = request.POST['Username']
		password = request.POST['Password']
		first = request.POST['first']
		last = request.POST['last']
		new_user=process_user(username, password, first, last)
		
		t = loader.get_template('users/signup-display.html')
		c = RequestContext(request, {'new_user':new_user})
	
		r = t.render(c)
	
		return HttpResponse(r)


def t2login(request):
	
	f = LoginForm()
	
	t = loader.get_template('users/login.html')
	c = RequestContext(request, {'f':f})
	
	r = t.render(c)
	
	return HttpResponse(r)
	

def t2login2(request):

	#May have to move the LoginForm down again to get it to "work"
	
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
			
	#return HttpResponse()
		
@login_required
def add_event(request):
	
	f = AddEventForm()
	
	t = loader.get_template('users/add-event.html')
	c = RequestContext(request, {'f':f})
	r = t.render(c)

	return HttpResponse(r)



@login_required
def t2addevent(request):
	
	#Needs to take information from the addevent form and dump it into the database
	
	return HttpResponse("Okay")







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
	r = t.render(c)
	
	return HttpResponse(r)

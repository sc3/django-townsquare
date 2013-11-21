from django.http import HttpResponse, HttpResponseRedirect
from square.models import Volunteer
from django.template import Context, Template, loader, RequestContext
from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def about(request):
	
	output = "About the Townsquare project:"
	return HttpResponse(output)


def t2login(request):
	
	class LoginForm(forms.Form):
		Username = forms.CharField()
		Password = forms.CharField(widget=forms.PasswordInput())
		
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
def home(request):
	
	#Assign the information on a single volunteer as an admin
	va = Volunteer.objects.get(id="2")
	
	#Loading template in "t" and assigning variable to context in "c"
	t = loader.get_template('users/index.html')
	c = RequestContext(request, {'va':va,})
	
	#Compiling template and rendering out the context information
	r = t.render(c)
	
	return HttpResponse(r)

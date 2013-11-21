from django.http import HttpResponse
from square.models import Volunteer
from django.template import Context, Template, loader, RequestContext
from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



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
		
		#import pdb; pdb.set_trace()
		
		if user is not None:
			
			if user.is_active:
				
				login(request, user)
				#Redirect to success page
				
				state="Logged in"
				
				return HttpResponse("Okay")
				#return HttpResponseRedirect('/volunteers/browse')
				
			else:
				
				return HttpResponse("Not valid")
				#Redirect to signup
				
		else:
			
			return HttpResponse("Sign Up")
			#Redirect to signup
			
	#return HttpResponse()
		

	
		

	
	
	
	
def home(request):
	
	#Assign the information on a single volunteer as an admin
	va = Volunteer.objects.get(id="2")
	
	#Loading template in "t" and assigning variable to context in "c"
	t = loader.get_template('users/index.html')
	c = RequestContext(request, {'va':va,})
	
	#Compiling template and rendering out the context information
	r = t.render(c)
	
	
	
	
	return HttpResponse(r)


def browse_volunteers(request):
    
    #Assigning information of all volunteers to a variable
    volunteers = Volunteer.objects.all()
    
    #Loading template in "t" and assigning variable to context in "c"
    t = loader.get_template('users/volunteer_browse.html')
    c = RequestContext(request, {'volunteers':volunteers,})
    
    #Compiling template and rendering out the context information
    r = t.render(c)
    
    #Returning the compiled template with rendered info to template
    return HttpResponse(r)
    
    
browse_volunteers.alters_data=False

def search_volunteers(request):
    output = "Which volunteer do you want to view?"
    return HttpResponse(output)

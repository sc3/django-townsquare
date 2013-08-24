from django.http import HttpResponse
from square.models import Volunteer
from django.template import Context, Template, loader, RequestContext
from django.shortcuts import render


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


def home(request):
	output="Welcome to Townsquare"
	
	return HttpResponse(output)

from django.http import HttpResponse
from square.models import Volunteer

def index(request):
    output = "Some cool stuff."
    return HttpResponse(output)

def browse_volunteers(request):
    output = "Here are all the volunteers. </br></br>"
    volunteers = Volunteer.objects.all()
    for volunteer in volunteers:
        output += "%s, hours worked: %s </br>" % (volunteer.name, volunteer.calculate_hours())
    return HttpResponse(output)

def search_volunteers(request):
    output = "Which volunteer do you want to view?"
    return HttpResponse(output)

def signup_volunteers(request):
    return HttpResponse("Start signing up volunteers here")

def create_event(request):
    return HttpResponse("Create event here")

def browse_events(request):
    return HttpResponse("Here are all the events")

def search_events(request):
    return HttpResponse("Which event do you want to view?")

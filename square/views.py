from django.http import HttpResponse
from square.models import Volunteer

def browse_volunteers(request):
    output = "Here are all the volunteers. </br></br>"
    volunteers = Volunteer.objects.all()
    for volunteer in volunteers:
        output += "%s, hours worked: %s </br>" % (volunteer.name, volunteer.calculate_hours())
    return HttpResponse(output)

def search_volunteers(request):
    output = "Which volunteer do you want to view?"
    return HttpResponse(output)

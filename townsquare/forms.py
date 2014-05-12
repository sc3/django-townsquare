
from django.forms import Form, ModelForm, CharField, PasswordInput, \
        BooleanField, ModelChoiceField, ChoiceField, SplitDateTimeField, \
        DateField, TimeField
from django.contrib.admin.widgets import AdminTimeWidget, AdminDateWidget

from townsquare.models import Event, EventLocation, Volunteer
from townsquare.models import initial_event_location

from datetime import datetime, time


class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

    # define a set of event locations,
    # and get or create an initial event location
    location = ModelChoiceField(
            label='Event Location',
            queryset=EventLocation.objects.all(), 
            initial=initial_event_location())



class VolunteerForm(ModelForm):

    class Meta:
        model = Volunteer
        exclude = ('user', )

    # Define additional fields besides those on the Volunteer Model,
    # so that we can handle user creation behind the scenes. 

    username = CharField(label='Username', required=False)
    permission = ChoiceField(label='Permission Level', initial=Volunteer.VOLUNTEER,
            choices=Volunteer.PERMISSION_GROUPS)
    password = CharField(label='New Password', 
            required=False, widget=PasswordInput())
    password_confirm = CharField(label='Re-enter Password', 
            required=False, widget=PasswordInput())

        
    
class LoginForm(Form):
        
    username = CharField(label='Username')
    password = CharField(label='Password', widget=PasswordInput())


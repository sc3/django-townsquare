
from django.forms import Form, ModelForm, CharField, PasswordInput, \
        BooleanField, ModelChoiceField, ChoiceField, SplitDateTimeField, \
        DateField, TimeField
from square.models import Event, EventLocation, Volunteer
from management.commands.initialize import initial_event_location
from datetime import datetime, time


class EventForm(ModelForm):
    type = ChoiceField(label='Event Type', initial='Open Build', choices=Event.EVENT_TYPES)
    date = DateField(label='Event Date', initial=datetime.today())
    start = TimeField(initial=time(11))
    end = TimeField(initial=time(17))
    location = ModelChoiceField(
            label='Event Location',
            queryset=EventLocation.objects.all(), 
            initial=initial_event_location())
    is_volunteer_time = BooleanField(required=False, initial=True)

    class Meta:
        model = Event
        fields = ['type', 'date', 'start', 'end', 'location', 'notes', 'is_volunteer_time']


class VolunteerForm(Form):
    
    first_name = CharField(label='First Name')
    last_name = CharField(label='Last Name')
    username = CharField(label='Username', required=False)
    permission = ChoiceField(label='Permission Level', initial='Volunteer',
            choices=Volunteer.PERMISSION_GROUPS)
    password = CharField(label='New Password', 
            required=False, widget=PasswordInput())
    password_confirm = CharField(label='Re-enter Password', 
            required=False, widget=PasswordInput())
    
    
class LoginForm(Form):
        
    username = CharField(label='Username')
    password = CharField(label='Password', widget=PasswordInput())


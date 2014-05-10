
from django.forms import Form, ModelForm, CharField, PasswordInput, \
        BooleanField, ModelChoiceField, ChoiceField, SplitDateTimeField, \
        DateField, TimeField
from django.contrib.admin.widgets import AdminTimeWidget, AdminDateWidget
from square.models import Event, EventLocation, Volunteer
from management.commands.initialize import initial_event_location
from datetime import datetime, time
from square.settings import DATE_INPUT_FORMATS


class EventForm(ModelForm):
    start = TimeField(initial=time(11), widget=AdminTimeWidget)
    end = TimeField(initial=time(17), widget=AdminTimeWidget)
    location = ModelChoiceField(
            label='Event Location',
            queryset=EventLocation.objects.all(), 
            initial=initial_event_location())

    class Meta:
        model = Event
        fields = ('type', 'date', 'start', 'end', 'location', 'notes', 'is_volunteer_time')


class VolunteerForm(ModelForm):
    
    username = CharField(label='Username', required=False)
    permission = ChoiceField(label='Permission Level', initial='Volunteer',
            choices=Volunteer.PERMISSION_GROUPS)
    password = CharField(label='New Password', 
            required=False, widget=PasswordInput())
    password_confirm = CharField(label='Re-enter Password', 
            required=False, widget=PasswordInput())

    class Meta:
        model = Volunteer
        fields = ('full_name', 'email', 'signup_date')
        
    
class LoginForm(Form):
        
    username = CharField(label='Username')
    password = CharField(label='Password', widget=PasswordInput())



from django.forms import Form, ModelForm, CharField, PasswordInput, \
        BooleanField, ModelChoiceField, DateTimeField, ChoiceField, SplitDateTimeField
from django.contrib.admin.widgets import AdminDateWidget 
from django.forms.widgets import SplitDateTimeWidget
from square.models import Event, EventLocation, Volunteer
from management.commands.initialize import initial_event_location
from datetime import datetime, time
from square.utils import time_today


class EventForm(ModelForm):
        
    is_volunteer_time = BooleanField(required=False, initial=True)
    event_type = ChoiceField(initial='Open Build', choices=Event.EVENT_TYPES)
    start = SplitDateTimeField(initial=time_today(11), widget=SplitDateTimeWidget)
    end = SplitDateTimeField(initial=time_today(17), widget=SplitDateTimeWidget)
    event_location = ModelChoiceField(queryset=EventLocation.objects.all(), 
            initial=initial_event_location())

    class Meta:
        model = Event
        fields = ('notes',)


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


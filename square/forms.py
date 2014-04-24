
from django.forms import Form, ModelForm, CharField, PasswordInput, \
        BooleanField, ModelChoiceField, DateField, ChoiceField
from django.contrib.admin.widgets import AdminDateWidget 
from square.models import Event, EventLocation, Volunteer


def initial_event_location():

    try:
        return EventLocation.objects.get(id=1)
    except EventLocation.DoesNotExist:
        el = EventLocation.objects.create(
            full_name='FreeGeek Chicago', 
            address='3411 W. Diversey Avenue',
            city='Chicago',
            state='IL',
            zip_code='60647'
        )
        el.save()
        return el


class EventForm(ModelForm):
        
    is_volunteer_time = BooleanField(required=False, initial=True)
    event_location = ModelChoiceField(queryset=EventLocation.objects.all(), 
                                        initial=initial_event_location())

    class Meta:
        model = Event
        fields = ('event_type', 'event_location', 'date', 'start',
                    'end', 'notes', 'is_volunteer_time')


class VolunteerForm(Form):
    
    first_name = CharField(label='First Name')
    # middle_initial = CharField(label='Middle Initial', required=False)
    last_name = CharField(label='Last Name')
    username = CharField(label='Username', required=False)
    password = CharField(label='Password', required=False, widget=PasswordInput())
    credentials = ChoiceField(label='Permission Level', choices=Volunteer.PERMISSION_GROUPS)
    
    
class LoginForm(Form):
        
    username = CharField(label='Username')
    password = CharField(label='Password', widget=PasswordInput())


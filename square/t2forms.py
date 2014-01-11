from django.forms import Form, ModelForm, CharField, PasswordInput, BooleanField
from square.models import Event, EventLocation

class AddEventForm(ModelForm):
	is_volunteer_time = BooleanField(required=False, initial=True)

	class Meta:
		model = Event
		fields = ['event_type', 'event_location', 'date',
					'start', 'end', 'notes', 'is_volunteer_time']


class SignupForm(Form):
	
	first = CharField(label='First Name')
	last = CharField(label='Last Name')
	Username = CharField()
	Password = CharField(widget=PasswordInput())
	
	
class LoginForm(Form):
		
	Username = CharField()
	Password = CharField(widget=PasswordInput())


#Need a form set to put in the sign in/sign out information (sessions)

class SessionForm(Form):
	
	session_events = Event.objects.all()
	
	
	
	

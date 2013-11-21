from django.forms import Form, ModelForm
from square.models import Event

class AddEventForm(ModelForm):

	class Meta:
		model = Event
		fields = ['event_type', 'event_location', 'date',
					'start', 'end', 'notes', 'is_volunteer_time']


class SignupForm(Form):
	
	first = forms.CharField(label='First Name')
	last = forms.CharField(label='Last Name')
	
	Username = forms.CharField()
	Password = forms.CharField(widget=forms.PasswordInput())
	
	
class LoginForm(Form):
		
	Username = forms.CharField()
	Password = forms.CharField(widget=forms.PasswordInput())

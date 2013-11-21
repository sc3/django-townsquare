from django import forms


class SignupForm(forms.Form):
	
	first = forms.CharField(label='First Name')
	last = forms.CharField(label='Last Name')
	
	Username = forms.CharField()
	Password = forms.CharField(widget=forms.PasswordInput())
	
	


class LoginForm(forms.Form):
		
	Username = forms.CharField()
	Password = forms.CharField(widget=forms.PasswordInput())

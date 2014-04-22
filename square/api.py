from copy import copy
import csv
import os

from django.http import HttpResponse

from django.contrib.auth.models import User

from tastypie import fields
from tastypie.exceptions import ApiFieldError, Unauthorized
from tastypie.fields import ToManyField, ToOneField
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from tastypie.serializers import Serializer

from square.models import Volunteer

class UserResource(ModelResource):
	
	class Meta:
		
		queryset = User.objects.all()
		resource_name = 'user'
		fields = ['first_name', 'last_name']


#Volunteer Model - main point of access
class VolunteerResource(ModelResource):
	
	user = fields.ForeignKey(UserResource, 'user', full=True)
	
	class Meta:
		
		queryset = Volunteer.objects.all()
		resource_name = 'volunteers'
		
		serializer = Serializer()
		



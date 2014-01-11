from copy import copy
import csv
import os

from django.http import HttpResponse

from tastypie.exceptions import ApiFieldError, Unauthorized
from tastypie.fields import ToManyField, ToOneField
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication

from django.conf.urls import patterns, include, url
from django.contrib import admin

#Defining the general URL schema for the application

admin.autodiscover()
urlpatterns = patterns('',
     url(r'^townsquare/', include('square.urls')),
     url(r'^admin/', include(admin.site.urls)),
     
)

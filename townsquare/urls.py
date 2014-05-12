from django.conf.urls import patterns, url, include
from django.contrib import admin

from townsquare import views
from townsquare.api import VolunteerResource, UserResource

from tastypie.api import Api

v1_api = Api(api_name="v1")
v1_api.register(UserResource())
v1_api.register(VolunteerResource())

#Defining the general URL schema for the application

admin.autodiscover()
urlpatterns = patterns('',

    # admin
    url(r'^admin/', include(admin.site.urls)),

    # volunteer
    url(r'^townsquare/about$', views.about),
    url(r'^townsquare/login$', views.t2login),

    # legacy
    url(r'^townsquare/volunteer/add$', views.add_volunteer),
    url(r'^townsquare/volunteer/browse$', views.browse_volunteers),
    url(r'^townsquare/volunteer/edit/(\d+)/$', views.edit_volunteer),
    url(r'^townsquare/event/add$', views.add_event),
    url(r'^townsquare/event/browse$', views.browse_events),
    url(r'^townsquare/event/edit$', views.edit_event),
    url(r'^townsquare/event/edit/(\d+)/$', views.edit_event),
     
)

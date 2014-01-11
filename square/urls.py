from django.conf.urls import patterns, url, include
from square import views
from square.api import VolunteerResource


volunteer_resource = VolunteerResource()


urlpatterns = patterns('',

    url(r'^about$', views.about),
    url(r'^login$', views.t2login),
    url(r'^logout$', views.t2logout),
    url(r'^volunteer/home$', views.home),
    url(r'^volunteer/add$', views.signup),
    url(r'^event/add$', views.add_event),
    url(r'^event/browse$', views.browse_events),
    url(r'^signup-success$', views.t2signup_success),
    url(r'^volunteer/browse$', views.browse_volunteers),
    url(r'^volunteer/search$', views.search_volunteers),

    # Processing views
    url(r'^event2$', views.t2addevent),
    
    #Data access
    url(r'^api/', include(volunteer_resource.urls)),
)

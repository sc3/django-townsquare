from django.conf.urls import patterns, url, include
from square import views
from square.api import VolunteerResource, UserResource
from tastypie.api import Api


v1_api = Api(api_name="v1")
v1_api.register(UserResource())
v1_api.register(VolunteerResource())


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

    # Processing views
    url(r'^event2$', views.t2addevent),
    
    #JSON for typeahead
    #url(r'^data/nhl.json$', views.nhl)
    url(r'^data/vol.json$', views.voljson),
    
    #Data access
    url(r'^api/', include(v1_api.urls)),
 
)

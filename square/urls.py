from django.conf.urls import patterns, url
from square import views

urlpatterns = patterns('',

    url(r'^about$', views.about),
    url(r'^login$', views.t2login),
    url(r'^logout$', views.t2logout),
    url(r'^volunteers/home$', views.home),
    url(r'^volunteer/add$', views.t2signup),
    url(r'^event/add$', views.add_event),

    # Processing views
    url(r'^login2$', views.t2login2),
    url(r'^signup2$', views.t2signup2),
    url(r'^event2$', views.t2addevent),
    
)

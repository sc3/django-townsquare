from django.conf.urls import patterns, url
from square import views

urlpatterns = patterns('',

    url(r'^about$', views.about),
    url(r'^login$', views.t2login),
    url(r'^logout$', views.t2logout),
    url(r'^volunteers/home$', views.home),
    url(r'^volunteer/add$', views.signup),
    url(r'^event/add$', views.add_event),
    url(r'^signup-success$', views.t2signup_success),
    url(r'^addevent-success$', views.t2addevent_success),
    
)

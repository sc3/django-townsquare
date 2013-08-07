from django.conf.urls import patterns, url
from square import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^volunteers/search$', views.search_volunteers),
    url(r'^volunteers/browse$', views.browse_volunteers),
    url(r'^volunteers/signup$', views.signup_volunteers),
    url(r'^events/create$', views.create_event),
    url(r'^events/search$', views.search_events)
)

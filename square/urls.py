from django.conf.urls import patterns, url
from square import views

urlpatterns = patterns('',
    url(r'^volunteers/search$', views.search_volunteers),
    url(r'^volunteers/browse$', views.browse_volunteers),
    url(r'^home$', views.home),
)

from django.conf.urls import patterns, url
from square import views

urlpatterns = patterns('',
    url(r'^volunteers/home$', views.home),
    url(r'^about$', views.about),
    url(r'^login$', views.t2login),
    url(r'^login2$', views.t2login2),
    
)

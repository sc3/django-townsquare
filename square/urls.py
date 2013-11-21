from django.conf.urls import patterns, url
from square import views

urlpatterns = patterns('',
    url(r'^volunteers/search$', views.search_volunteers),
    url(r'^volunteers/browse$', views.browse_volunteers),
    url(r'^volunteers/home$', views.home),
    url(r'^about$', views.about),
    #Changed the loaded view to the built in login form from views.t2login
    #url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^login$', views.t2login),
    #url(r'^login$', views.t2login2),
    url(r'^login2$', views.t2login2),
)

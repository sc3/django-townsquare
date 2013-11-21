from django.conf.urls import patterns, url
from square import views

urlpatterns = patterns('',
    url(r'^volunteers/home$', views.home),
    
    url(r'^about$', views.about),
    
    url(r'^login$', views.t2login),
    
    #Processing for t2login
    url(r'^login2$', views.t2login2),
    
    url(r'^volunteer/add$', views.t2signup),
    
    #Processing for t2signup
    url(r'^signup2$', views.t2signup2),
    
    url(r'^logout$', views.t2logout),
    
    url(r'^event/add$', views.add_event),
    url(r'^event2/add$', views.t2_addevent),
    
    
    
    
)

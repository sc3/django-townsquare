from django.contrib import admin
from square.models import Event, EventLocation, Session, Volunteer

admin.site.register(Session)
admin.site.register(Event)
admin.site.register(EventLocation)
admin.site.register(Volunteer)

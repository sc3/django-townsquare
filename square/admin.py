from django.contrib import admin
from square.models import Event, EventLocation, Session, Volunteer

class SessionInline(admin.TabularInline):
    model = Session
    extra = 1

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Info', {'fields' : ['type', 'event_location']}),
    	('Time Info',  {'fields' : ['date', 'start', 'end']}),
        ('Other',      {'fields' : ['notes'], 'classes': ['collapse']}),
    ]
    inlines = [SessionInline]

admin.site.register(Event, EventAdmin)
admin.site.register(EventLocation)
admin.site.register(Volunteer)

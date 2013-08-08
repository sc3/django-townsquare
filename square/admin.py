from django.contrib import admin
from square.models import Event, EventLocation, Session, Volunteer

class SessionInline(admin.TabularInline):
    model = Session
    extra = 1

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('What and Where is it?',      {'fields': ['type', 'event_location']}),
    	('When is it?',       {'fields': ['date', 'start', 'end']}),
        ('Additional Info', {'fields': ['notes', 'volunteer_time'], 		    
	    'classes': ['collapse']}),
    ]
    inlines = [SessionInline]
    list_display = ('type', 'date', 'event_location', 'volunteer_time')

admin.site.register(Event, EventAdmin)
admin.site.register(Volunteer)
admin.site.register(EventLocation)

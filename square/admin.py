from django.contrib import admin
from square.models import Event, EventLocation, Session, Volunteer
from square.forms import EventForm, VolunteerForm

class SessionInline(admin.TabularInline):
    model = Session
    extra = 1


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('What and Where is it?', {'fields': ['event_type', 'event_location']}),
    	('When is it?',           {'fields': ['date', 'start', 'end']}),
        ('Additional Info',       {'fields': ['notes', 'is_volunteer_time'], 'classes': ['collapse']}),
    ]
    inlines = [SessionInline]
    list_display = ('event_type', 'date', 'event_location')
    form = EventForm


class VolunteerAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'signup_date', 'hours')
    search_fields = ['full_name']

    readonly_fields = ('hours', 'credit')
    fieldsets = [
    	('Personal Info', 	{'fields': ['first_name', 'last_name']}),
    	('Legacy Info',     {'fields': ['signup_date', 'hours']}),
    ]    


admin.site.register(Event, EventAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(EventLocation)

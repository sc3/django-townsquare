from django.contrib import admin
from square.models import Event, EventLocation, Session, Volunteer

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



'''class VolunteerAdmin(admin.ModelAdmin):
    readonly_fields = ('hours',)
    fieldsets = [
        ('Personal Info',   {'fields': ['name', 'email']}),
    	('Legacy Info',     {'fields': ['signup_date', 'hours']}),
    ]
    list_display = ('name', 'signup_date', 'hours', 'email')
    search_fields = ['name']'''


admin.site.register(Event, EventAdmin)
#admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(EventLocation)

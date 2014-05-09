from django.contrib import admin
from square.models import Event, EventLocation, Session, Volunteer
from square.forms import EventForm, VolunteerForm

class SessionInline(admin.TabularInline):
    model = Session
    extra = 1


class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('total_participants', 'total_service_hours')
    fieldsets = (
        ('Summary', {
                'fields': (('total_participants', 'total_service_hours'), )
        }), 
        ('Event Details', {
            'classes': ('collapse',),
            'fields': ('date', ('start', 'end'), 'location', 'notes', 'is_volunteer_time'),
        })
    )
    inlines = [SessionInline]
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

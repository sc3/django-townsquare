from django.contrib import admin
from square.models import Event, EventLocation, Session, Volunteer
from square.forms import EventForm, VolunteerForm

class SessionInline(admin.TabularInline):
    model = Session
    extra = 1


class EventAdmin(admin.ModelAdmin):

    list_display = ('type', 'date', 'total_participants', 'total_service_hours')
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

    list_display = ('full_name', 'signup_date', 'hours', 'credit')
    search_fields = ['full_name']

    readonly_fields = ('hours', 'credit')
    fieldsets = (
    	('Basic', {
            'fields': ('full_name', 'email')
        }),
        ('Emergency Contact', {
            'fields': ('contact_name', 'contact_relationship', 
                        'contact_phone_number')
        }),
        ('Account', {
            'fields': ('username', 'password', 'password_confirm', 
                        'permission')
        }),
        ('Volunteer', {
            'fields': ('signup_date', 'hours', 'credit')
        })
    )    

    form = VolunteerForm


admin.site.register(Event, EventAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(EventLocation)

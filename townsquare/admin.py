from django.contrib import admin
from townsquare.models import Event, EventLocation, Session, Volunteer
from townsquare.forms import EventForm, VolunteerForm

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
            'fields': ('type', 'date', ('start', 'end'), 'location', 'notes', 'is_volunteer_time'),
        })
    )
    inlines = [SessionInline]
    form = EventForm


class VolunteerAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'signup_date', 'hours', 'credit')
    search_fields = ['full_name']

    readonly_fields = ('hours', 'credit')
    fieldsets = (
    	('Basic Information', {
            'fields': ('full_name', 'email', 'hours', 'credit')
        }),
        ('Account Information', {
            'fields': ('username', 'password', 'password_confirm', 
                        'permission')
        }),
        ('Additional', {
            'fields': ('signup_date', 'legal_date', 'birth_date', 'conduct_notes', 'medical_notes'),
            # 'classes': ('collapse',)
        }),
        ('Emergency Contact', {
            'fields': ('contact_name', 'contact_relationship', 
                        'contact_phone_number'),
            # 'classes': ('collapse',)
        }),
    )    

    form = VolunteerForm


admin.site.register(Event, EventAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(EventLocation)

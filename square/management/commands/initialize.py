
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.utils import IntegrityError
from django.core.management import call_command
from django.core.management.base import BaseCommand

from square.models import EventLocation


###########################
# Permissions
###########################


APP_NAME = 'square'

def get_ct(content_name):
    result = ContentType.objects.filter(app_label=APP_NAME, name=content_name)
    if not result:
        raise Exception('No such content type exists.')
    else:
        return result[0]

def get_perm_by_ct(contenttype):
    return Permission.objects.filter(content_type__in=contenttype)

def create_new_group(name, ct_names):

    group, _ = Group.objects.get_or_create(name=name)

    group_cts = []
    group_perms = []

    for ct_name in ct_names:
        group_cts.append(get_ct(ct_name))

    for perm in get_perm_by_ct(group_cts):
        group_perms.append(perm)

    group.permissions.add(*group_perms) 
    group.save()


##########################
# Event Location
##########################


def initial_event_location():

    try:
        return EventLocation.objects.get(id=1)
    except EventLocation.DoesNotExist:
        el = EventLocation.objects.create(
            full_name='FreeGeek Chicago', 
            address='3411 W. Diversey Avenue',
            city='Chicago',
            state='IL',
            zip_code='60647'
        )
        el.save()
        return el


class Command(BaseCommand):

    args = "No args accepted for now"
    help = "Initializes a Townsquare instance"

    def handle(self, *args, **options):

        # make sure database schema is setup 
        call_command("syncdb")
        call_command("migrate")

        # create permission groups
        create_new_group('Staff', ('session', 'event', 'event location', 'volunteer'))
        create_new_group('Admin', ('session', 'event', 'event location'))
        create_new_group('Volunteer', ())

        # create initial event location
        initial_event_location()






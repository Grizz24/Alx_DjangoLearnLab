from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book  # or whatever model you added permissions to

class Command(BaseCommand):
    help = "Set up default groups and permissions"

    def handle(self, *args, **kwargs):
        # Create groups
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        editors, _ = Group.objects.get_or_create(name="Editors")
        admins, _ = Group.objects.get_or_create(name="Admins")

        # Grab the permissions you created in the model
        can_view = Permission.objects.get(codename="can_view")
        can_create = Permission.objects.get(codename="can_create")
        can_edit = Permission.objects.get(codename="can_edit")
        can_delete = Permission.objects.get(codename="can_delete")

        # Assign permissions
        viewers.permissions.set([can_view])
        editors.permissions.set([can_view, can_create, can_edit])
        admins.permissions.set([can_view, can_create, can_edit, can_delete])

        self.stdout.write(self.style.SUCCESS("Groups and permissions set up successfully!"))

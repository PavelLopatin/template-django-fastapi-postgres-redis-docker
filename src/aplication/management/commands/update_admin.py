from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('--email', type=str, default='')

    def handle(self, *args, **options):
        user_model = get_user_model()
        message = None
        try:
            user = user_model.objects.get(username=options["username"])
            if not user.check_password(options["password"]):
                user.set_password(options["password"])
                user.save()
                message = "[INFO] Admin password has been updated"
        except user_model.DoesNotExist:
            user = user_model(
                username=options["username"],
                email=options["email"],
                is_superuser=True,
                is_staff=True
            )
            user.set_password(options["password"])
            user.save()
            message = "[INFO] Admin has been created"
        return message

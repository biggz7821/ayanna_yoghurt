from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Create a default superuser (only if it doesn't exist)"

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'admin'
        email = 'admin@ayannayoghurt.com'
        password = 'linet7821'   # ← change this if you want

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(
                f"Superuser created → {username} / {password}"
            ))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser already exists"))

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ayannayoghurt.settings")
django.setup()

from django.contrib.auth.models import User

# delete existing admin
User.objects.filter(username="admin").delete()

# create new admin
User.objects.create_superuser(
    username="admin",
    email="admin@ayannayoghurt.com",
    password="admin"
)

print("Admin reset successful!")

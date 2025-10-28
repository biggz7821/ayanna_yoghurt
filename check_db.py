import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ayannayoghurt.settings')
django.setup()

from django.contrib.auth.models import User
from django.db import connection

print(f"Database: {connection.settings_dict['ENGINE']}")
print(f"Users in database: {User.objects.count()}")

for user in User.objects.all():
    print(f"User: {user.username} (staff: {user.is_staff}, superuser: {user.is_superuser})")

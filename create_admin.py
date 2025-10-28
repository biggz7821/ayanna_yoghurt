import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ayannayoghurt.settings')
django.setup()

from django.contrib.auth.models import User

# Delete any existing admin user
User.objects.filter(username='admin').delete()

# Create new admin user
User.objects.create_superuser(
    username='admin',
    email='admin@ayannayoghurt.com', 
    password='Ayanna2024!'
)

print("✅ ADMIN USER FORCE CREATED!")
print("🌐 Website: https://ayannayoghurt.onrender.com/admin/")
print("👤 Username: admin")
print("🔑 Password: Ayanna2024!")

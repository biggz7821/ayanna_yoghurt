import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ayannayoghurt.settings')
django.setup()

from django.contrib.auth.models import User

# Delete ALL admin users first
User.objects.filter(username='admin').delete()

# Create with simple password
user = User.objects.create_superuser('admin', 'admin@ayannayoghurt.com', 'admin')
user.save()

print("🎉 ADMIN USER CREATED!")
print("📍 https://ayannayoghurt.onrender.com/admin/")
print("👤 admin")
print("🔑 admin")

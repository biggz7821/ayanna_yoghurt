#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Force create admin in PostgreSQL
python manage.py shell -c "
from django.contrib.auth.models import User
User.objects.filter(username='admin').delete()  # Remove old admin
User.objects.create_superuser('admin', 'admin@ayannayoghurt.com', 'admin123')
print('✅ ADMIN FORCE CREATED FOR ayannayoghurt.onrender.com')
print('✅ Login: https://ayannayoghurt.onrender.com/admin/')
print('✅ Username: admin')
print('✅ Password: admin123')
"

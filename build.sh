#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Force create admin user in PostgreSQL
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@ayannayoghurt.com', 'Ayanna2024!')
    print('🎉 ADMIN USER CREATED SUCCESSFULLY!')
    print('📍 Website: https://ayannayoghurt.onrender.com')
    print('👤 Username: admin')
    print('🔑 Password: admin123')
else:
    print('✅ Admin user already exists in PostgreSQL database')
"

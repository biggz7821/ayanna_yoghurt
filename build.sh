#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Create admin in NEW database
python manage.py shell -c "
from django.contrib.auth.models import User
from django.db import connection

print('🆕 FRESH DATABASE SETUP')
print('📊 Database:', connection.settings_dict['NAME'])
print('🔧 Engine:', connection.settings_dict['ENGINE'])

# Create admin user
User.objects.create_superuser('admin', 'admin@ayannayoghurt.com', 'admin123')

print('✅ ADMIN USER CREATED SUCCESSFULLY!')
print('🌐 Login: https://ayannayoghurt.onrender.com/admin/')
print('👤 Username: admin')
print('🔑 Password: admin123')
print('')
print('🎉 YOUR ADMIN IS READY!')
"

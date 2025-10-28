#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# Force PostgreSQL migrations
python manage.py migrate --database=default
python check_db.py
# Create admin in PostgreSQL
python manage.py shell -c "
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ayannayoghurt.settings'
import django
django.setup()

from django.contrib.auth.models import User
from django.db import connections

# Check which database we're using
db_engine = connections['default'].settings_dict['ENGINE']
print(f'Using database: {db_engine}')

# Create admin
User.objects.filter(username='admin').delete()
User.objects.create_superuser('admin', 'admin@ayannayoghurt.com', 'admin')
print('✅ ADMIN CREATED IN POSTGRESQL')
print('👤 Username: admin')
print('🔑 Password: admin')
"

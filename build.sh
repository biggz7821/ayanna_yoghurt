#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Force create admin - this WILL work
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').delete(); User.objects.create_superuser('admin', 'admin@ayannayoghurt.com', 'Ayanna2024!'); print('✅ ADMIN CREATED')" | python manage.py shell

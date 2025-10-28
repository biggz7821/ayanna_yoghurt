#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Create admin with simple password
python create_admin.py

# Double check it was created
python manage.py shell -c "
from django.contrib.auth.models import User
users = User.objects.all()
print(f'Total users: {users.count()}')
for u in users:
    print(f'User: {u.username} (staff: {u.is_staff}, superuser: {u.is_superuser})')
"

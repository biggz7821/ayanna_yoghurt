"""
Django settings for ayannayoghurt project.
"""
import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ayanna-yoghurt-secret-key-2024'
DEBUG = True

ALLOWED_HOSTS = [
    'ayannayoghurt.onrender.com',
    'localhost',
    '127.0.0.1',
]

CSRF_TRUSTED_ORIGINS = [
    'https://ayannayoghurt.onrender.com',
    'https://*.onrender.com',
]

# ✅ NEW DATABASE URL
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://ayannayoghurt_db_user:AgmKfVn5EgENCRN6BGvtnQcZX3tlYVaI@dpg-d40944n5r7bs73a9fvlg-a.oregon-postgres.render.com/ayannayoghurt_db',
        conn_max_age=600
    )
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ayannayoghurt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
TIME_ZONE = 'Africa/Nairobi'
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

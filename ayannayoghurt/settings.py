"""
Django settings for ayannayoghurt project.
"""
import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ayanna-yoghurt-secret-key-2024'
DEBUG = True

# Your domain
ALLOWED_HOSTS = [
    'ayannayoghurt.onrender.com',
    'localhost',
    '127.0.0.1',
]

# CSRF for your domain
CSRF_TRUSTED_ORIGINS = [
    'https://ayannayoghurt.onrender.com',
    'https://*.onrender.com',
]

# ✅ YOUR POSTGRESQL DATABASE
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://ayanna_db_user:Ym4z2MAaS9NBylqXhyZQ3XiEjHax0W51@dpg-d3qkinqli9vc73cesjpg-a/ayanna_db',
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

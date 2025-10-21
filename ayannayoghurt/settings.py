"""
Django settings for ayannayoghurt project.
"""
import os
import dj_database_url  # ✅ ADD THIS IMPORT
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ayanna-yoghurt-secret-key-2024'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# ✅ CRITICAL: Use your CURRENT domain until you change it
CSRF_TRUSTED_ORIGINS = [
    'https://ayanna-yoghurt-1.onrender.com',  # ← YOUR CURRENT DOMAIN
    'https://ayannayoghurt.onrender.com',     # ← YOUR DESIRED DOMAIN
    'https://*.onrender.com',
]

# ✅ SECURITY SETTINGS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'

# ✅ POSTGRESQL DATABASE - FIXES DATA LOSS
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://ayanna_db_user:Ym4z2MAaS9NBylqXhyZQ3XiEjHax0W51@dpg-d3qkinqli9vc73cesjpg-a/ayanna_db',
        conn_max_age=600
    )
}

# Application definition
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

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Time zone
TIME_ZONE = 'Africa/Nairobi'
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

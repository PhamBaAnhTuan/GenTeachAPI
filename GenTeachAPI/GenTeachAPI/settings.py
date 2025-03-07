"""
Django settings for GenTeachAPI project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h835bd1hwm&c0x5j+ni1mjkg96ev!&9r8ddtfa!5d8f%6&l_q4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'genteachapi.onrender.com',
    'localhost',
    '127.0.0.1',
    '192.168.93.143',    #phone
    '192.168.1.5',      #home
    '192.168.31.188',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'oauth2_provider',
    'corsheaders',
    
    'user',
    'chat',
    'shop',
    'video',
    'study',
    'podcast',
]

OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope', 
        'write': 'Write scope', 
        'admin': 'Admin scope',
    },
    # 'ACCESS_TOKEN_EXPIRE_SECONDS': 36000,  # Access token expiration time
    # 'REFRESH_TOKEN_EXPIRE_SECONDS': 1209600,  # Refresh token expiration time
    'ROTATE_REFRESH_TOKENS': True,  # Rotate refresh tokens on use
    'APPLICATION_MODEL': 'oauth2_provider.Application',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

OAUTH2_PROVIDER = {
    "ACCESS_TOKEN_EXPIRE_SECONDS": 86400,  # 1 day
    "REFRESH_TOKEN_EXPIRE_SECONDS": 86400,  # 1 day
    "ROTATE_REFRESH_TOKEN": True,  # Set True to issue new refresh tokens on use
}

ROOT_URLCONF = 'GenTeachAPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'GenTeachAPI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'GenTeachDB',
    #     'USER': os.getenv('USER'),
    #     'PASSWORD': os.getenv('PASSWORD'),
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

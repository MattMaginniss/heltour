"""
Django settings for heltour project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os


ADMINS = []

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gje)lme+inrew)s%@2mvhj+0$vip^n500i22-o23lm$t1)aq8e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'www.lichess4545.tv',
    'lichess4545.tv',
    'heltour.lakin.ca',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'heltour.tournament',
    'reversion',
    'bootstrap3',
    'ckeditor',
    'debug_toolbar',
    'memoize',
]

MIDDLEWARE_CLASSES = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'heltour.urls'

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

WSGI_APPLICATION = 'heltour.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'heltour_lichess4545',
        'USER': 'heltour_lichess4545',
        'PASSWORD': 'sown shuts combiner chattels',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

BOOTSTRAP3 = {
    'set_placeholder': False
}

LOGIN_URL = '/admin/login/'

DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ['127.0.0.1', '::1']

GOOGLE_SERVICE_ACCOUNT_KEYFILE_PATH = '/etc/heltour/gspread.conf'
JAVAFO_COMMAND = 'java -jar /etc/heltour/javafo.jar'

# Host-based settings overrides.
import platform
import re
try:
    hostname = platform.node().split('.')[0]
    exec 'from .local.%s import *' % re.sub('[^\w]', '_', hostname)
except ImportError:
    pass # ignore missing local settings

# Allow live settings (which aren't in the repository) to override the development settings.
import os
import json
if os.path.exists("/etc/heltour/production.json"):
    overrides = json.loads(open("/etc/heltour/production.json", "r").read())
    DATABASES = overrides.get("DATABASES", DATABASES)
    ADMINS = overrides.get("ADMINS", locals().get('ADMINS'))
    EMAIL_HOST = overrides.get("EMAIL_HOST", locals().get('EMAIL_HOST'))
    EMAIL_PORT = overrides.get("EMAIL_PORT", locals().get('EMAIL_PORT'))
    EMAIL_USE_TLS = overrides.get("EMAIL_USE_TLS", locals().get('EMAIL_USE_TLS'))
    EMAIL_HOST_USER = overrides.get("EMAIL_HOST_USER", locals().get('EMAIL_HOST_USER'))
    EMAIL_HOST_PASSWORD = overrides.get("EMAIL_HOST_PASSWORD", locals().get('EMAIL_HOST_PASSWORD'))
    SERVER_EMAIL = overrides.get("SERVER_EMAIL", locals().get('SERVER_EMAIL'))
    GOOGLE_SERVICE_ACCOUNT_KEYFILE_PATH = overrides.get("GOOGLE_SERVICE_ACCOUNT_KEYFILE_PATH", GOOGLE_SERVICE_ACCOUNT_KEYFILE_PATH)

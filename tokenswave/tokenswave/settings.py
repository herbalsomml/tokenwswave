from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os
from dotenv import load_dotenv
import json



load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = os.getenv('DJANGO_DEBUG')

ALLOWED_HOSTS = json.loads(os.environ['ALLOWED_HOSTS'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tokenswave.urls'

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

WSGI_APPLICATION = 'tokenswave.wsgi.application'

DATABASES = {}

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

LANGUAGES = [
    ('en', _('English')),
    ('id', _('Bahasa')),
    ('de', _('Deutsch')),
    ('es', _('Español')),
    ('fr', _('Français')),
    ('hi', _('हिन्दी (Hindī)')),
    ('it', _('Italiano')),
    ('cs', _('Čeština')),
    ('lv', _('Latviski')),
    ('hu', _('Magyar nyelv')),
    ('ko', _('한국어 (Hangugeo)')),
    ('ru', _('Русский')),
    ('ja', _('日本語 (Nihongo)')),
    ('pl', _('Polski')),
    ('uk', _('Українська')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


domain = os.getenv('DOMAIN')
sitename = os.getenv('SITENAME')
twitter = os.getenv('TWITTER')
telegram = os.getenv('TELEGRAM')
snapchat = os.getenv('SNAPCHAT')
google_analytics = os.getenv('GOOGLE_ANALYTICS')
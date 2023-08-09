"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-md5l46pf$@t8sc^u%&-plpfp3j9aym7x1env4(f1z5calzaxp6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    "django_apscheduler",
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'deb': {
            "format": '{asctime} :: {levelname} :: {message}',
            'style' : '{',
        },

        'war': {
            "format": '{asctime} :: {levelname} :: {message} :: {pathname}',
            'style' : '{',
        },

        'err': {
            "format": '{asctime} :: {levelname} :: {message} :: {pathname} :: {exc_info}',
            'style' : '{',
        },

        'gen': {
            "format": '{asctime} :: {levelname} :: {module} :: {message}',
            'style' : '{',
        },

        'mail': {
            "format": '{asctime} :: {levelname} :: {message} :: {pathname}',
            'style' : '{',
        },
    },

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },

        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'handlers': {
        'deb': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            "class": "logging.StreamHandler",
            "formatter": "deb",
        },
        'war': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            "class": "logging.StreamHandler",
            "formatter": "war",
        },
        'err': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            "class": "logging.StreamHandler",
            "formatter": 'err',
        },
        'gen': {
            "level": "INFO",
            'filters': ['require_debug_false'],
            "formatter": 'gen',
            "class": "logging.FileHandler",
            "filename": "./logs/general.log",
        },

        'err_f': {
            'level': 'ERROR',
            "class": "logging.FileHandler",
            "formatter": 'err',
            "filename": "./logs/errors.log",
        },

        'sec': {
            'level': 'DEBUG',
            "formatter": 'gen',
            "class": "logging.FileHandler",
            "filename": "./logs/security.log",
        },

        'mail_admins': {
            'level': 'ERROR',
            "formatter": 'mail',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {

        "django.request": {
            "handlers": ["err_f", 'mail_admins'],
            "level": "ERROR",
            "propagate": True,
        },
        'django': {
            'handlers': ['deb', "war", 'err', 'gen'],
            'level': 'DEBUG',
            'propagate': True,
        },
        "django.server": {
            "handlers": ["err_f", 'mail_admins'],
            "level": "ERROR",
            "propagate": True,
        },
        "django.template": {
            "handlers": ["err_f"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.backends": {
            "handlers": ["err_f"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security": {
            "handlers": ["sec"],
            'level': 'DEBUG',
            "propagate": True,
        },
    }
}

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = "/news"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "newsportal1"
EMAIL_HOST_PASSWORD = "jrayxuhjdxaikcnw"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "newsportal1@yandex.ru"

SERVER_EMAIL = "newsportal1@yandex.ru"

MANAGERS = (
    ('иван', 'ivan.busalaev@yandex.ru'),
    ('иван', 'ikb2012bik@gmail.com'),
)

ADMINS = (
    ('иван', 'ivan.busalaev@yandex.ru'),
)

APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'
APSCHEDULER_RUN_NOW_TIMEOUT = 25
SITE_URL = 'http://127.0.0.1:8000'


CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
        'TIMEOUT': 30,
    }
}
"""
Django settings for students_proj project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from students_proj import db  # Якщо у вас цей рядок - помилка, то вам слід додати спеціально приховане поле
#                               DATABASES у директорію students_proj
from students_proj.db import SOCIALACCOUNT_PROVIDERS, ADMIN_EMAIL
from students_proj.db import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_HOST, EMAIL_USE_SSL, EMAIL_USE_TLS



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5^4owm4mg12gu_tkb%g@^kg&tkn*@@(s9+xe9p_3k8$+%ex9@)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 3rd party apps
    'crispy_forms',               # crispy_forms must be added!
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',

    # project apps
    'students',
    'students_proj',
]

# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     'facebook': {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         'APP': {
#             'client_id': '********************',
#             'secret': '******************************',
#         }
#     },
#     'github': {
#         'APP': {
#             'client_id': '**********************',
#             'secret': '***********************************',
#         }
#     }
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'students_proj.urls'

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
                'students_proj.context_processors.students_proc',
                'students.context_processors.groups_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'students_proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = db.DATABASES  # додаєте свою базу даних.

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

SITE_ID = 1  # ідентифікатор сайту (для allauth!)

LOGIN_REDIRECT_URL = 'home'   # Після вдалої автентифікації редіректимо користувача на список студентів

ACCOUNT_LOGOUT_ON_GET = True  # Дозволити робити логаут за допомогою GET запиту

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MAX_UPLOAD_SIZE = 2097152  # 2MB


# STATICFILES_DIRS = [
#     "/home/special.polls.com/polls/static",
#     "/home/polls.com/polls/static",
#     "/opt/webfiles/common",
# ]


# email settings
# please, set here you smtp server details and your admin email

# ADMIN_EMAIL = '****************@gmail.com'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = '**************@gmail.com'
# EMAIL_HOST_PASSWORD = '*********************'
# EMAIL_PORT = 465
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True


CRISPY_TEMPLATE_PACK = 'bootstrap4'  # settings of Django Crispy Forms

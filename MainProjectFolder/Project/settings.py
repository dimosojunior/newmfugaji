"""
Django settings for pollme project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
from pathlib import Path
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import timedelta
import datetime
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


from dotenv import load_dotenv
load_dotenv()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'x*za6xf&_80ofdpae!yzq61g9ffikkx9$*iygbl$j7rr4wlf8t'
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','mfugajismart.net','www.mfugajismart.net','137.184.204.91']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',  #swagger documentation
    #'ckeditor',
    'djoser',
    'django_apscheduler',
    #'ckeditor_uploader',
    'corsheaders', #to connect django and react
    'App',
    'MyTemplatesApp',
    'AddAppViewSets',
    'accounts.apps.AccountsConfig',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'Project.wsgi.application'
AUTH_USER_MODEL="App.MyUser"

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mfugajismartdb',
        'USER':'mfugajismart',
        'PASSWORD':'Dimoso@9898',
        'HOST':'localhost',
        'PORT':'',
    }
}




# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'Asia/Dhaka'
# #TIME_ZONE = 'African/dar_es_salaam'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True



TIME_ZONE = 'Africa/Dar_es_Salaam'
#TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/



STATIC_URL = '/static/'
#STATICFILES_DIRS = [
    #os.path.join(BASE_DIR, 'static')


STATIC_ROOT = BASE_DIR / "MyTemplatesApp/static"
# CRISPY_TEMPLATE_PACK = "bootstrap4"



MEDIA_URL = "/media/"
MEDIA_ROOT= BASE_DIR / "media"
# Default primary key field type

# CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
# CKEDITOR_UPLOAD_PATH = 'media/'

# CKEDITOR_CONFIGS = {
#     'default' : {
#         'toolbar': 'full',
#         'height': 400,
#         'width': '100%',
#     }
# }


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dimosoeljunior8@gmail.com'
EMAIL_HOST_PASSWORD = 'rrqvntxaattupawv'
EMAIL_USE_TLS = True
"""
Django settings for ch12 project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%u0^l=@#5+iagtz-e1ode@x2y!h#dr2@82h5av97romtot-jya'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite',
    'captcha',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'easy_thumbnails',
    'filer',
    'mptt',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ch12.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'ch12.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
# Fill with your own info
MAILGUN_SERVER_NAME = ''
MAILGUN_ACCESS_KEY = ''

ACCOUNT_ACTIVATION_DAYS = 7

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = [
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
]

FILER_STORAGES = {
    'public':{
        'main':{
            'ENGINE':'filer.storage.PublicFileSystemStorage',
            'OPTIONS':{
                'location':'/home/zs/django16/ch12/media/filer',
                'base_url':'/media/filer/'
            },
            'UPLOAD_TO':'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX':'filer_public'
        },
        'thumbnails':{
            'ENGINE':'filer.storage.PublicFileSystemStorage',
            'OPTIONS':{
                'location':'/home/zs/django16/ch12/media/filer_thumbnails',
                'base_url':'/media/filer_thumbnails/',
            },
        },
    },
    'private':{
        'main':{
            'ENGINE':'filer.storage.PrivateFileSystemStorage',
            'OPTIONS':{
                'location':'/home/zs/django16/ch12/media/filer',
                'base_url':'/smedia/filer/'
            },
            'UPLOAD_TO':'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX':'filer_public'
        },
        'thumbnails':{
            'ENGINE':'filer.storage.PrivateFileSystemStorage',
            'OPTIONS':{
                'location':'/home/zs/django16/ch12/media/filer_thumbnails',
                'base_url':'/smedia/filer_thumbnails/',
            },
        },
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/zs/django16/ch12/media'
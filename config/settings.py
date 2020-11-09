"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#gitなどでシークレットキー流出を防ぐため。local_settings.pyにSECRET_KEYを指定、読み込ませる
SECRET_KEY = "シークレットキー文字列を入力する"
try:
    from .local_settings import *
except ImportError:
    pass


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG   = True
HEROKU  = False

ALLOWED_HOSTS = [ "127.0.0.1" ]
# Application definition

#DBを使用するアプリを読み込む

#django.contrib.humanizeはカンマ区切り用
#django.contrib.sitesからallauth.socialaccountはdjango-allauth用。django-allauthに関しては実践編のP30を参照
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
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

ROOT_URLCONF = 'config.urls'


#'DIRS'にos.path.join(BASE_DIR,"templates")を含める
#allauthのテンプレートを読み込ませる
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,"templates"),
            ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/


#CODEはja、TIME_ZONEはAsia/Tokyoを指定
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL  = '/static/'

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

#デプロイ後の静的ファイルの指定
"""
PROJECT_NAME = os.path.basename(BASE_DIR)
STATIC_ROOT = '/var/www/{}/static'.format(PROJECT_NAME)

STATIC = "/var/www/{}/static".format(PROJECT_NAME)
"""

#====================heroku setting=======================================
#この部分はherokuにデプロイするときの設定
if HEROKU:
    import django_heroku
    import dj_database_url
    ALLOWED_HOSTS = [ '' ]
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
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME'      : '',
                'USER'      : '',
                'PASSWORD'  : '',
                'HOST'      : '',
                'PORT': '5432',
                }
            }
    db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default'].update(db_from_env)
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

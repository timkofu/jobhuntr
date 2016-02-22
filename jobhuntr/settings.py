
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import dj_database_url
import dj_redis_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z0cgj)r!bwho6v3kuofewse7n$*(2(cs18&nzyqg(%+p-3u+7n'

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('PRODUCTION'):
    DEBUG = False
    DBCONF = dj_database_url.parse(os.environ.get("DATABASE_URL"))
    cache_vars = dj_redis_url.parse(os.environ.get("REDIS_URL"))
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': '{0}:{1}'.format(cache_vars['HOST'],cache_vars['PORT']),
            'OPTIONS': {
                'DB': cache_vars['DB'],
                'PASSWORD': cache_vars['PASSWORD'],
                'PARSER_CLASS': 'redis.connection.HiredisParser',
                'CONNECTION_POOL_CLASS':'redis.BlockingConnectionPool',
                'CONNECTION_POOL_CLASS_KWARGS': {
                    'max_connections': 19,
                    'timeout': 20,
                }
            },
        }
    }
    ALLOWED_HOSTS = ['jobhunt-r.herokuapp.com']
else:
    DEBUG = True
    DBCONF = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'jobhuntr.sqlite3'),
    }

# HayStack backend
NEEDLE = {
    'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
}


# Application definition

INSTALLED_APPS = (
    'flat',  # flat-theme
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'haystack',
    'watson',  # admin full-text-search
    'daterange_filter',

    'search',
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

ROOT_URLCONF = 'jobhuntr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        #'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
            ('django.template.loaders.cached.Loader', [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]),
        ],
        },
    },
]

WSGI_APPLICATION = 'jobhuntr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': DBCONF
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = False # using naive datetimes


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_global'),
)

ADMINS = (
    ('Tim', 'makobu.mwambiriro@gmail.com'),
)

# HayStack
HAYSTACK_CONNECTIONS = {
    'default': NEEDLE
}

# Email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("MANDRILL_USERNAME")
EMAIL_HOST_PASSWORD = os.environ.get("MANDRILL_KEY")


# Disable emails on DISALLOWED_HOSTS hit
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    },
}

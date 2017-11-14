

import os
from urllib.parse import urlparse

import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if os.environ.get("PRODUCTION"):
    DEBUG = False
    ALLOWED_HOSTS = [
        "jobhunt-r.herokuapp.com",
    ]
    SECRET_KEY = os.getenv("SECRET_KEY")
    DB = dj_database_url.parse(os.environ['DATABASE_URL'], conn_max_age=600)
else:
    DEBUG = True
    SECRET_KEY = 'z0cgj)r!bwho6v3kuofewse7n$*(2(cs18&nzyqg(%+p-3u+7n'
    DB = None


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'haystack',
    'daterange_filter',
    'channels',

    'search',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if not DEBUG:  # # SSLify
    MIDDLEWARE_CLASSES.insert(0, 'sslify.middleware.SSLifyMiddleware')

ROOT_URLCONF = 'jobhuntr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'jobhuntr.wsgi.application'


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


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': DB or {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jobhuntr',
        'USER': 'jobhuntr',
    }
}


# Log me out after 15 minutes of inactivity
SESSION_COOKIE_AGE = 60*15
SESSION_COOKIE_SECURE = False if DEBUG else True # Ensure HTTPS
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv('REDIS_CLOUD', 'redis://localhost:6379'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 20},
            # Configs below recommended for speed here
            # https://www.peterbe.com/plog/fastest-redis-optimization-for-django
            "PARSER_CLASS": "redis.connection.HiredisParser",
            #"SERIALIZER": "django_redis.serializers.msgpack.MSGPackSerializer", # defaults to pickle
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        }
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = False # using naive datetimes


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_global'),
)
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ADMINS = (
    ('Tim', 'makobu.mwambiriro@gmail.com'),
)


# Email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("GMAIL_EMAIL")
EMAIL_HOST_PASSWORD = os.getenv("APP_SPECIFIC_PASSWORD")


# Disable email on DISALLOWED_HOSTS hit
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


#** App Specific Configs **#

# HayStack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    }
}


# Django Channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.getenv('REDIS_URL', 'redis://localhost:6379')],
        },
        "ROUTING": "jobhuntr.routing.channel_routing",
    },
}

# My Settings
MAX_JOB_AGE = 14

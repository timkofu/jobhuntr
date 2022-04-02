import os

import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if os.environ.get("PRODUCTION"):
    DEBUG = False
    ALLOWED_HOSTS = [
        f"{os.getenv('APP_NAME')}.herokuapp.com",  # Name of your app
    ]
    SECRET_KEY = os.getenv("SECRET_KEY")
else:
    DEBUG = True
    SECRET_KEY = "z0cgj)r!bwho6v3kuofewse7n$*(2(cs18&nzyqg(%+p-3u+7n"


INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "haystack",
    "search",
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "jobhuntr.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "jobhuntr.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


DATABASES = {
    "default": dj_database_url.parse(os.getenv("DATABASE_URL"), conn_max_age=600)
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Log me out after 15 minutes of inactivity
SESSION_COOKIE_AGE = 60 * 15
SESSION_COOKIE_SECURE = False if DEBUG else True  # Ensure HTTPS
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_CLOUD", "redis://localhost:6379"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 20},
            # Configs below recommended for speed here
            # https://www.peterbe.com/plog/fastest-redis-optimization-for-django
            "PARSER_CLASS": "redis.connection.HiredisParser",
            # "SERIALIZER": "django_redis.serializers.msgpack.MSGPackSerializer", # defaults to pickle
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        },
    }
}


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_L10N = True

USE_TZ = False


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_global"),)

ADMINS = (("Tim", "makobu.mwambiriro@gmail.com"),)


# Email
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("GMAIL_EMAIL")
EMAIL_HOST_PASSWORD = os.getenv("APP_SPECIFIC_PASSWORD")


# Disable email on DISALLOWED_HOSTS hit
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "null": {
            "class": "logging.NullHandler",
        },
    },
    "loggers": {
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
    },
}


# ** App Specific Configs **#

# HayStack
HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.simple_backend.SimpleEngine",
    }
}

# My Settings
MAX_JOB_AGE = 14

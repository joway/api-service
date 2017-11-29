import datetime
import os

from corsheaders.defaults import default_headers

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY', 'xxx')

DEBUG = False
if DEBUG == os.environ.get('DEBUG', 'False'):
    DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_REGEX_WHITELIST = (
#     r'^(https?://)?localhost',
#     r'^(https?://)?127.0.0.1',
# )

CORS_ALLOW_CREDENTIALS = True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'jet',
    'jet.dashboard',
    'django.contrib.admin',
    'raven.contrib.django.raven_compat',

    'telegram',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console', ],
        'level': os.getenv('LOG_LEVEL', 'INFO'),
        'propagate': True,
    },
}

# DATABASES = {
#     'default': {
#         'NAME': os.environ.get('MYSQL_INSTANCE_NAME'),
#         'ENGINE': 'django.db.backends.mysql',
#         'USER': os.environ.get("MYSQL_USERNAME"),
#         'PASSWORD': os.environ.get("MYSQL_PASSWORD"),
#         'HOST': os.environ.get("MYSQL_HOST"),
#         'PORT': os.environ.get("MYSQL_PORT", 3306),
#         'CONN_MAX_AGE': int(os.environ.get('CONN_MAX_AGE', 60 * 10)),
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#             'init_command': 'SET sql_mode=\'STRICT_TRANS_TABLES\'',
#         },
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('db.sqlite3'),
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': int(os.environ.get('CONN_MAX_AGE', 60 * 3)),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-hans'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/stk/'
STATIC_ROOT = 'collected_static'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'user.auth.CookieAuthentication',
    # ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'PAGE_SIZE': 100,
}
# AUTH_USER_MODEL = 'user.User'

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://{0}:6379/{1}".format(
#             os.environ.get('REDIS_HOST', 'authcenter.drg3w2.0001.cnn1.cache.amazonaws.com.cn'),
#             os.environ.get('REDIS_DB', '1'),
#         ),
#         'TIMEOUT': 60 * 60,  # seconds
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100},
#         }
#     }
# }

try:
    from .local_settings import *
except Exception as e:
    print('loading local settings failed:', e)
    pass

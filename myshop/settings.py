"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 4.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^o@4h9*tok$kx6ui=w_@l9obihm=al=$^n^_rw%rifiqdn^ed("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "jet",  # Тюнинг админки
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_spectacular",  # Автогенерация документации Open API
    "social_django",  # Авторизация с социальной сетью
    "imagekit",  # Создание миниатюр картинок
    "cacheops",  # Кэширование запросов к БД
    "shop",  # Основное приложение магазина
    "cart",  # Приложение для покупательской корзины
    "orders",  # Приложение для оформления заказа
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = "myshop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "cart.context_processors.cart",  # процессор контекста для корзины
            ],
        },
    },
]

WSGI_APPLICATION = "myshop.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / 'staticfiles'  # Это для автоматической сборки статических файлов

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

CART_SESSION_ID = 'cart'  # ключ для хранения корзины в пользовательском сеансе

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # писать электронные письма в консоль

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# Конфигурация для VK
AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_VK_OAUTH2_KEY = '8228531'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'KfAqQA9fweZJoTB1N7HZ'
LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/auth/'

# Конфигурация для Celery
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Используем Redis в качестве брокера сообщений
CELERY_ACCEPT_CONTENT = ['json']  # Формат сообщений Celery
CELERY_TASK_SERIALIZER = 'json'   # Сериализация задач в формат JSON
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # Хранение результатов также в Redis
CELERY_TIMEZONE = 'UTC'  # Настройка временной зоны


# Конфигурация для Sentry
sentry_sdk.init(
    dsn="https://061ceec07364da8c16fa6c740211c9fb@o4507830617440256.ingest.de.sentry.io/4507830621896784",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,  # Настройка уровня выборки событий для производительности (по умолчанию 1.0)
    send_default_pii=True    # Опционально: отправлять личную идентифицируемую информацию (PII)
)

# Конфигурация для Redis
# Настройки кэша
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # URL и порт сервера Redis
    }
}


# Настройки Cacheops
CACHEOPS_REDIS = {
    'host': 'localhost',  # Адрес Redis сервера
    'port': 6379,         # Порт Redis
    'db': 1,              # Номер базы данных Redis
    'socket_timeout': 3,  # Таймаут соединения
}


# Настройки Cacheops
CACHEOPS = {
    'default': {
        'timeout': 60 * 15,  # Время кэширования в секундах (15 минут)
        'ops': {
            'all': True,
        },
    },
    'shop.Category': {'ops': 'all', 'timeout': 60 * 15},
    'shop.Product': {'ops': 'all', 'timeout': 60 * 15},
    'orders.Order': {'ops': 'all', 'timeout': 60 * 15},
    'orders.OrderItem': {'ops': 'all', 'timeout': 60 * 15},
}

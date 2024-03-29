"""
Django settings for blog_python_django_project project.

Generated by 'django-admin startproject' using Django 4.1.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_i-bp_4+or1@o@eb5zpd4-)=u@771#*ry&f^#0=4_-vdk=&kki'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # При переходе в производственную среду следует помнить о том, что необходимо устанавливать его значение равным False

ALLOWED_HOSTS = [] # не применяется при включенном режиме отладки или при выполнении тестов.


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', # сайт администрирования
    'django.contrib.auth', # фреймворк аутентификации
    'django.contrib.contenttypes', # фреймворк типов контента
    'django.contrib.sessions', # фреймворк сеансов (сессий?)
    'django.contrib.messages', # фреймворк сообщений
    'django.contrib.staticfiles', # фреймворк управления статическими файлами
    'blog_app.apps.BlogConfig', # конфиг приложения и Django увидит и сможет загружать модели приложения
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

ROOT_URLCONF = 'blog_python_django_project.urls'

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

WSGI_APPLICATION = 'blog_python_django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC' # TODO: доработать чтобы было местное время +5 Екб. Но может быть баг, если в админке пост создается во время 3 часа ночи по Екб, то при нажатии на новый пост на странице, будет переход с ошибкой (//урл:порт/блог/дата27число), а если ввести (//урл:порт/блог/дата26число), то ошибки не будет. Надо продебажить и понять мб не хватает при создании точного времени +5 и именно поэтому достается там дата со временем +0, а не +5, затем образеается и у нас число другое

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

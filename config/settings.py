# Copyright (c) 2020 by Abdullah Alnuaimi
# SPDX-License-Identifier: MIT

import os

from configurations import Configuration


class Base(Configuration):

    DEBUG = True
    SECRET_KEY = 'secret'
    ALLOWED_HOSTS = ['*']

    ATOMIC_REQUESTS = True
    X_FRAME_OPTIONS = 'SAMEORIGIN'

    DJANGO_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django.contrib.flatpages',
    ]

    SITE_ID = 1

    THIRD_PARTY_APPS = [
        'widget_tweaks',
        'django_filters',
    ]

    LOCAL_APPS = [
        'apps.products',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.middleware.gzip.GZipMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'config.urls'
    WSGI_APPLICATION = 'config.wsgi.application'

    # base Django admin URL (should be something obscure in production)

    ADMIN_URL = 'admin/'

    # Django filter

    FILTERS_EMPTY_CHOICE_LABEL = None

    # Password validation
    # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/3.0/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    @property
    def BASE_DIR(self):
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @property
    def INSTALLED_APPS(self):
        return self.DJANGO_APPS + self.THIRD_PARTY_APPS + self.LOCAL_APPS

    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

    @property
    def DATABASES(self):
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(self.BASE_DIR, 'db.sqlite3'),
            }
        }

    @property
    def TEMPLATES(self):
        return [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    os.path.join(self.BASE_DIR, 'templates')
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

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.0/howto/static-files/

    @property
    def STATICFILES_DIRS(self):
        return [os.path.join(self.BASE_DIR, 'static')]

    @property
    def STATIC_URL(self):
        return '/static/'

    @property
    def STATIC_ROOT(self):
        return os.path.join(self.BASE_DIR, 'staticfiles')

    @property
    def MEDIA_URL(self):
        return '/media/'

    @property
    def MEDIA_ROOT(self):
        return os.path.join(self.BASE_DIR, 'media')


class Testing(Base):
    pass


class Local(Base):

    THIRD_PARTY_APPS = Base.THIRD_PARTY_APPS + [
        'debug_toolbar',
    ]

    MIDDLEWARE = Base.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': ['debug_toolbar.panels.redirects.RedirectsPanel'],
        'SHOW_TEMPLATE_CONTEXT': True,
    }

    INTERNAL_IPS = [
        '127.0.0.1',
    ]


class Production(Base):

    from decouple import config

    DEBUG = False
    SECRET_KEY = config('SECRET_KEY')
    ALLOWED_HOSTS = ['fashis.herokuapp.com']

    ADMIN_URL = config('ADMIN_URL')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
        }
    }

    import dj_database_url

    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

    # This is required for Heroku SSL.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Stream logging to stdout: use `heroku log` to view
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {'console': {'class': 'logging.StreamHandler'}},
        'loggers': {'root': {'handlers': ['console'], 'level': 'INFO'}},
    }

"""
Django settings for quiz_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def root(x):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), x)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')in33+y(6bv#$+uknqj*oa+7exgxv8=rsy823)af*7ipsu7$&c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.contrib.messages.context_processors.messages',
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
)

# Application definition

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quiz_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'quiz_project.urls'

WSGI_APPLICATION = 'quiz_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'quiz.db'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quiz',
        'USER': 'postgres_simplans',
        'PASSWORD': 'josearun',
        'HOST': 'localhost',
        'PORT': '5432',                      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_ROOT = '/home/simplans/zorse_projects/quiz_project/media/'


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"

STATIC_ROOT = '/home/simplans/zorse_projects/quiz_project/static/'
STATIC_URL = '/static/'


# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
#   STATIC_URL = '/static/'
STATICFILES_DIRS = (
    '/home/simplans/zorse_projects/quiz_project/staticdirs/',

    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
TEMPLATE_DIRS = (
    root('templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


GRAPPELLI_ADMIN_TITLE = 'Quiz Site'
GRAPPELLI_INDEX_DASHBOARD = 'quiz_project.dashboard.CustomIndexDashboard'
# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Walt Askew', 'waltaskew@gmail.com'),
)

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

MANAGERS = ADMINS

REGISTRATION_SECRET = 'foo'

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'djangoappengine',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'djangotoolbox',
    'accounts',
    'problems',
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
STATICFILES_ROOT = os.path.join(os.path.dirname(__file__), '_generated_media')
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
)
STATICFILES_URL = '/site_media/'
MEDIA_URL = '/site_media/uploads/'
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

SITE_ID = 1

# Activate django-dbindexer if available
try:
    import dbindexer
    DATABASES['native'] = DATABASES['default']
    DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
    INSTALLED_APPS += ('dbindexer',)
except ImportError:
    pass

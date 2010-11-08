# -*- coding: utf-8 -*-
import os

HOME_DIR = os.path.dirname( __file__ )

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Lech Twaróg', 'lech.twarog@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': os.path.join( HOME_DIR, 'test.db' ),			   # Or path to database file if using sqlite3.
		'USER': '',						 # Not used with sqlite3.
		'PASSWORD': '',					 # Not used with sqlite3.
		'HOST': '',						 # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',						 # Set to empty string for default. Not used with sqlite3.
	},
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Warsaw'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join( HOME_DIR, 'media/' )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qt#vj_k0u=_vty11q^aqc-61e(o*_6!kim8fge98+g9w)up8uw'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.csrf.CsrfResponseMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'cumulumbus.urls'

TEMPLATE_DIRS = (
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	os.path.join( HOME_DIR, 'templates' )
)


gettext = lambda s: s

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.i18n',
	'django.core.context_processors.request',
	'django.core.context_processors.media',
)

LANGUAGES = (
	( 'pl', gettext( 'Polski' ) ),
)

AUTH_PROFILE_MODULE = 'cumulumbus.core.models.UserProfile'

SERVICES = (
	'cumulumbus.service.rss.RSSService',
	'cumulumbus.service.soup.SoupService',
	'cumulumbus.service.lastfm.LastfmService',
)

LASTFM_API_KEY = '09f55b97093f0710d5b3e7011a633209'
LASTFM_API_SECRET = '123cd374125c909b4f6c3e37e8259052'

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.comments',
	'django.contrib.markup',
	'django.contrib.messages',
	'django.contrib.humanize',
	
	'south',
	'tagging',
	'pagination',
	'easy_thumbnails',
	'notification',
	'django_extensions',

	'cumulumbus.core',

	'cumulumbus.service.rss',
	'cumulumbus.service.soup',
	'cumulumbus.service.lastfm',
)

try:
	from settings_local import *
except ImportError:
	pass

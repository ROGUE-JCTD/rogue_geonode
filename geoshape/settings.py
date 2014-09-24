# -*- coding: utf-8 -*-

import geonode
import os

from geonode.settings import *  # noqa

SITENAME = 'GeoSHAPE'

# Defines the directory that contains the settings file as the PROJECT_ROOT
# It is used for relative settings elsewhere.
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
GEONODE_ROOT = os.path.abspath(os.path.dirname(geonode.__file__))

# Setting debug to true makes Django serve static media and
# present pretty error pages.
ALLOWED_HOSTS = ()
CACHE_TIME = 0
CLASSIFICATION_BANNER_ENABLED = False
DEBUG = TEMPLATE_DEBUG = True
GEOGIT_DATASTORE_NAME = 'DEFAULT_NAME'
LOCKDOWN_GEONODE = True
REGISTRATION_OPEN = False
SOCIAL_BUTTONS = False
MODIFY_TOPICCATEGORY = False
# Set to True to load non-minified versions of (static) client dependencies
DEBUG_STATIC = False

# This is needed for integration tests, they require
# geonode to be listening for GeoServer auth requests.


# Defines settings for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'development.db'),
    }
}

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default': {
        'BACKEND': 'geonode.geoserver',
        'LOCATION': 'http://localhost:8080/geoserver/',
        'PUBLIC_LOCATION': 'http://localhost:8080/geoserver/',
        'USER': 'admin',
        'PASSWORD': 'geoserver',
        'MAPFISH_PRINT_ENABLED': True,
        'PRINTNG_ENABLED': True,
        'GEONODE_SECURITY_ENABLED': True,
        'GEOGIT_ENABLED': True,
        'WMST_ENABLED': False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED': False,
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE': '',
        'TIMEOUT': 10,  # The maximum time to wait for the server to respond.
    }
}

# Uploader Settings
UPLOADER = {
    'BACKEND': 'geonode.rest',
    'OPTIONS': {
        'TIME_ENABLED': False,
        'GEOGIT_ENABLED': True,
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

WSGI_APPLICATION = "geoshape.wsgi.application"

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static"),
    os.path.join(GEONODE_ROOT, "static"),
]

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(GEONODE_ROOT, "templates"),
)

# Location of translation files
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, "locale"),
    os.path.join(GEONODE_ROOT, "locale"),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'x-#u&4x2k*$0-60fywnm5&^+&a!pd-ajrx(z@twth%i7^+oskh'

# Location of url mappings
ROOT_URLCONF = 'geoshape.urls'

MAX_DOCUMENT_SIZE = 2  # MB


INSTALLED_APPS = (
    'django.contrib.gis',
    'geoshape.file_service',
    'geoshape.core',
    'django_classification_banner',
    'maploom',
    'iaff_geoshape'
) + INSTALLED_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(name)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(message)s'},
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'ERROR',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
        },
        "geoshape": {
            "handlers": ["console", "mail_admins"],
            "level": "DEBUG",
        },
        "geonode": {
            "handlers": ["console", "mail_admins"],
            "level": "DEBUG",
        },
        "iaff_geoshape": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
        },
        "gsconfig.catalog": {
            "handlers": ["console"],
            "level": "ERROR",
        },
        "owslib": {
            "handlers": ["console"],
            "level": "ERROR",
        },
        "pycsw": {
            "handlers": ["console"],
            "level": "ERROR",
        },
        'south': {
            "handlers": ["console"],
            "level": "ERROR",
        },
    },
}

TEMPLATE_CONTEXT_PROCESSORS += (
    'django_classification_banner.context_processors.classification',
    'geoshape.core.context_processors.security_warnings'
)

# Add additional paths (as regular expressions) that don't require authentication.
AUTH_EXEMPT_URLS = ('/file-service/*', '/i18n/setlang/',)

if LOCKDOWN_GEONODE:
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('geonode.security.middleware.LoginRequiredMiddleware',)

# Load more settings from a file called local_settings.py if it exists
try:
    from local_settings import *  # noqa
except ImportError:
    pass

MAP_BASELAYERS = [
    {
        "source": {
            "ptype": "gxp_wmscsource",
            "url": OGC_SERVER['default']['LOCATION'] + "wms",
            "restUrl": "/gs/rest",
            "name": "local geoserver"
        }
    },
    {
        "source": {"ptype": "gxp_osmsource", "name": "OpenStreetMap"},
        "type": "OpenLayers.Layer.OSM",
        "name": "mapnik",
        "title": "OpenStreetMap",
        "args": ["OpenStreetMap"],
        "visibility": True,
        "fixed": True,
        "group":"background"
    }
]

DATABASE_ROUTERS = ['iaff_geoshape.routers.IAFFGeoRouter',]

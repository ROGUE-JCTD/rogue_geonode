# -*- coding: utf-8 -*-

import geonode
import os

from geonode.settings import *  # noqa

SITENAME = 'rogue_geonode'

LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

ALLOWED_HOSTS = ()
CACHE_TIME = 0
CLASSIFICATION_BANNER_ENABLED = False
DEBUG = TEMPLATE_DEBUG = True
GEOGIT_DATASTORE_NAME = 'DEFAULT_NAME'
LOCKDOWN_GEONODE = True
REGISTRATION_OPEN = False
SOCIAL_BUTTONS = False

# Set to True to load non-minified versions of (static) client dependencies
DEBUG_STATIC = False

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
        'LOCATION': 'http://localhost:8000/geoserver/',
        # PUBLIC_LOCATION needs to be kept like this because in dev mode
        # the proxy won't work and the integration tests will fail
        # the entire block has to be overridden in the local_settings
        'PUBLIC_LOCATION': 'http://localhost:8000/geoserver/',
        'USER': 'admin',
        'PASSWORD': 'geoserver',
        'MAPFISH_PRINT_ENABLED': True,
        'PRINT_NG_ENABLED': True,
        'GEONODE_SECURITY_ENABLED': True,
        'GEOGIT_ENABLED': True,
        'WMST_ENABLED': False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED': True,
        'GEOGIT_DATASTORE_DIR': '/var/lib/geoserver_data/geogit',
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE': '',  # 'datastore',
        'TIMEOUT': 10  # number of seconds to allow for HTTP requests
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

<<<<<<< HEAD:geoshape/settings.py
WSGI_APPLICATION = "geoshape.wsgi.application"


LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
) + LOCALE_PATHS

STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'x-#u&4x2k*$0-60fywnm5&^+&a!pd-ajrx(z@twth%i7^+oskh'

# Location of url mappings
ROOT_URLCONF = 'geoshape.urls'

INSTALLED_APPS = (
    'geonode.contrib.geogit',
    'geoshape.file_service',
    'geoshape.core',
    'django_classification_banner',
    'maploom',
    'south'
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
            "handlers": ["console"],
            "level": "ERROR",
        },
        "rogue_geonode": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "geonode": {
            "handlers": ["console"],
            "level": "DEBUG",
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
    'geoshape.core.context_processors.security_warnings',
    'geoshape.core.context_processors.rogue'
)

# Add additional paths (as regular expressions) that don't require authentication.
AUTH_EXEMPT_URLS = ('/file-service/*', '/i18n/setlang/',)

if LOCKDOWN_GEONODE:
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('geonode.security.middleware.LoginRequiredMiddleware',)


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



LEAFLET_CONFIG = {
    'TILES': [
        # Find tiles at:
        # http://leaflet-extras.github.io/leaflet-providers/preview/


        ('Basemap',
         'https://{s}.tiles.mapbox.com/v3/examples.map-i87786ca/{z}/{x}/{y}.png',
         '<a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; \
          <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, \
          <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'),
        ('OpenStreetMap HOT',
         'http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
         'Map tiles by <a href="http://hot.openstreetmap.org">Humanitarian OpenStreetMap Team</a>, \
         <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; \
         <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, \
         <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'),
    ],
    'PLUGINS': {
        'esri-leaflet': {
            'js': 'lib/js/esri-leaflet.js',
            'auto-include': True,
        },
    }
}


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

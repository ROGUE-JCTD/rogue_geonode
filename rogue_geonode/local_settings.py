# Uploader backend (rest or importer)

UPLOADER_BACKEND_URL = 'importer'

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'geonode',
         'USER': 'geonode',
         'PASSWORD': 'geonode',
     }
}

# GeoNode vector data backend configuration.

#Import uploaded shapefiles into a database such as PostGIS?
DB_DATASTORE = True

UPLOADER_SHOW_TIME_STEP=False

#Database datastore connection settings
DB_DATASTORE_DATABASE = 'geonode_imports'
DB_DATASTORE_USER = 'geonode'
DB_DATASTORE_PASSWORD = 'geonode'
DB_DATASTORE_HOST = 'localhost'
DB_DATASTORE_PORT = '5432'
DB_DATASTORE_TYPE = 'postgis'
DB_DATASTORE_NAME = 'geonode_imports'

#Database datastore connection settings
#GEOGIT_DATASTORE_NAME = 'geogit-repo'

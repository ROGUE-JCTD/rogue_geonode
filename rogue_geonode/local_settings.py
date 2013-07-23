# Uploader backend (rest or importer)

UPLOADER_BACKEND_URL = 'importer'

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': '<APPLICATION_DB_NAME>',
         'USER': '<APPLICATION_USER_NAME>',
         'PASSWORD': '<APPLICATION_USER_PASSWORD>',
	 'HOST': '<APPLICATION_DB_HOST>',
	 'PORT': '<APPLICATION_DB_PORT>',
     }
}

# GeoNode vector data backend configuration.

#Import uploaded shapefiles into a database such as PostGIS?
DB_DATASTORE = True

UPLOADER_SHOW_TIME_STEP = True

#Database datastore connection settings
DB_DATASTORE_DATABASE = '<DB_DATASTORE_DATABASE>'
DB_DATASTORE_USER = '<DB_DATASTORE_USER>'
DB_DATASTORE_PASSWORD = '<DB_DATASTORE_PASSWORD>'
DB_DATASTORE_HOST = '<DB_DATASTORE_HOST>'
DB_DATASTORE_PORT = '<DB_DATASTORE_PORT>'
DB_DATASTORE_TYPE = '<DB_DATASTORE_TYPE>'
DB_DATASTORE_NAME = '<DB_DATASTORE_NAME>'

#Database datastore connection settings
GEOGIT_DATASTORE_NAME = 'geogit-repo'
GEOGIT_DATASTORE = True

# Use the printNG geoserver lib
PRINTNG_ENABLED=True

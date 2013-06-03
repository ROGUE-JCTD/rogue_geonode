ROGUE GeoNode
=============

ROGUE GeoNode Project.

 * Custom GeoServer
 * Salamti GXP Client

Installation
------------

You will need to start with a GeoNode production or development setup. You can follow GeoNode's development or production setup instructions here https://github.com/GeoNode/geonode/blob/master/README

With GeoNode's virtualenv activated in development or production mode, do the following::

    $ git clone https://github.com/ROGUE-JCTD/rogue_geonode.git
    $ cd rogue_geonode 
    $ paver build # OPTIONAL Build a geoserver.war
    $ paver setup # Download a pre-built geoserver.war
    $ paver start

In production, you can modify the 'geonode' binary tool and geonode.wsgi file to point to this one.

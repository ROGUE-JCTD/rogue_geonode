Rogue_Geonode
========================

You should write some docs, it's good for the soul.

Installation
------------

With GeoNode's virtualenv activated in development or production mode, do the following::


    $ git clone https://github.com/ROGUE-JCTD/rogue_geonode.git
    $ pip install -e rogue_geonode 
    $ cd rogue_geonode
    $ paver setup # Download a pre-built geoserver.war
    $ # -or-
    $ paver build # Build a geoserver.war
    $ paver start 

In production, you can modify the 'geonode' binary tool and geonode.wsgi file to point to this one.

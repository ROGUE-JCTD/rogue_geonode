Rogue_Geonode
========================

You should write some docs, it's good for the soul.

Installation
------------

With GeoNode's virtualenv activated in development or production mode, do the following::


    $ git clone https://github.com/ROGUE-JCTD/rogue_geonode.git
    $ cd rogue_geonode
    $ pip install -e .
    $ python manage.py syncdb 
    $ python manage.py runserver

To install on a virtual environment do::

    $ pip install -e rogue_geonode

In production, you can modify the 'geonode' binary tool and geonode.wsgi file to point to this one.

#!/bin/bash

# For this to work perform the following command to change permissions
# sudo chmod 755 -R /var/lib/geonode;
sudo -u www-data -g www-data /var/lib/geonode/bin/uwsgi --ini /var/lib/geonode/rogue_geonode/django.ini

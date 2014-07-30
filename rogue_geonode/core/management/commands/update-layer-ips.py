#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Update the IP of local map layers'

    def handle(self, *args, **options):
        from geonode.maps.models import MapLayer
        from geonode.layers.models import Layer
        from django.conf import settings
        from urlparse import urlsplit

        layers = Layer.objects.exclude(storeType='remoteStore')
        if layers.count():
            oldurl = urlsplit(layers[0].distribution_url).netloc
            newurl = urlsplit(settings.OGC_SERVER['default']['PUBLIC_LOCATION']).netloc
            for layer in layers:
                layer.distribution_url = layer.distribution_url.replace(oldurl, newurl)
                linkset = layer.link_set.all()
                for link in linkset:
                    link.url = link.url.replace(oldurl, newurl)
                    link.save()
                layer.save()

        map_layers = MapLayer.objects.filter(local=True)
        if map_layers.count():
            oldurl = urlsplit(map_layers[0].ows_url).netloc
            newurl = urlsplit(settings.OGC_SERVER['default']['PUBLIC_LOCATION']).netloc
            for maplayer in map_layers:
                maplayer.ows_url = maplayer.ows_url.replace(oldurl, newurl)
                maplayer.save()

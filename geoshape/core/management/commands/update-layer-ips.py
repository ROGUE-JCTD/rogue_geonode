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
from django.core.exceptions import MultipleObjectsReturned
from geonode.maps.models import MapLayer
from geonode.layers.models import Layer
from django.conf import settings
from urlparse import urlsplit

class Command(BaseCommand):
    help = 'Update the IP of local map layers'

    @staticmethod
    def replaceNetLoc(old_url, new_netloc):
        old_netloc = urlsplit(old_url).netloc
        return old_url.replace(old_netloc, new_netloc)

    def handle(self, *args, **options):
        new_netloc = urlsplit(settings.OGC_SERVER['default']['PUBLIC_LOCATION']).netloc
        map_layers = MapLayer.objects.filter(local=True).exclude(ows_url__icontains=new_netloc)
        layers = Layer.objects.exclude(storeType='remoteStore')

        for maplayer in map_layers:
            new_url = self.replaceNetLoc(maplayer.ows_url, new_netloc)
            self.stdout.write('Changing map layer url from {0} to {1}. (Map Layer #{2})'
                              .format(maplayer.ows_url, new_url, maplayer.id))
            maplayer.ows_url = new_url
            maplayer.save()

        for layer in layers:
            for link in layer.link_set.all().exclude(url__isnull=True).exclude(url__icontains=new_netloc):
                new_url = self.replaceNetLoc(link.url, new_netloc)
                self.stdout.write('Updating the url for the "{0}" link on layer {1} from {2} to {3}'.format(
                    link.name, layer.name, link.url, new_url))
                link.url = self.replaceNetLoc(link.url, new_netloc)
                link.save()

        for layer in layers.exclude(distribution_url__isnull=True).exclude(distribution_url__icontains=new_netloc):
            new_url = self.replaceNetLoc(layer.distribution_url, new_netloc)
            self.stdout.write('Changing a layer distribution url from {0} to {1}. (Layer #{2})'.format(
                layer.distribution_url, new_url, layer.id))
            layer.distribution_url = new_url
            try:
                layer.save()
            except MultipleObjectsReturned:
                self.stdout.write('MultipleObjectsReturned Error when updating layer #{0}'.format(layer.id))

        for layer in layers.exclude(thumbnail_url__isnull=True).exclude(thumbnail_url__icontains=new_netloc):
            new_url = self.replaceNetLoc(layer.thumbnail_url, new_netloc)
            self.stdout.write('Changing a layer thumbnail url from {0} to {1}. (Layer #{2})'.format(
                layer.thumbnail_url, new_url, layer.id))
            layer.thumbnail_url = new_url
            try:
                layer.save()
            except MultipleObjectsReturned:
                self.stdout.write('MultipleObjectsReturned Error when updating layer #{0}'.format(layer.id))

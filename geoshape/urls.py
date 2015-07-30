from django.conf.urls import patterns, include
from geonode.urls import urlpatterns as geonode_url_patterns
from maploom.geonode.urls import urlpatterns as maploom_urls
from tilebundler.api import TilesetResource

tileset_resource = TilesetResource()

urlpatterns = patterns(
    '',
    (r'^file-service/', include('geoshape.file_service.urls')),
    (r'^gsschema/', include('gsschema.urls')),
    (r'^tileset/', include('tilebundler.urls', namespace='tilesets')),
    (r'^api/', include(tileset_resource.urls)),
    (r'^proxy/', 'geoshape.views.proxy')
)

urlpatterns += geonode_url_patterns
urlpatterns += maploom_urls

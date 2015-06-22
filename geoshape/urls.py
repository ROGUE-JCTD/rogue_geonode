from django.conf.urls import patterns, include
from geonode.urls import urlpatterns as geonode_url_patterns
from maploom.geonode.urls import urlpatterns as maploom_urls

urlpatterns = patterns('',
                       (r'^file-service/', include('geoshape.file_service.urls')),
                       (r'^tileset/', include('tilebundler.urls', namespace='tilesets')),
                       (r'^proxy/', 'geoshape.views.proxy'),
                       )

urlpatterns += geonode_url_patterns
urlpatterns += maploom_urls

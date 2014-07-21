from django.conf.urls import url, patterns, include
from geonode.urls import urlpatterns as geonode_url_patterns
from maploom.geonode.urls import urlpatterns as maploom_urls

urlpatterns = patterns('',
                       (r'^file-service/', include('rogue_geonode.file_service.urls')),
                       (r'^proxy/', 'rogue_geonode.views.proxy'),
                       )

urlpatterns += geonode_url_patterns
urlpatterns += maploom_urls

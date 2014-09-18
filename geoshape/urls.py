from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from geonode.urls import urlpatterns as geonode_url_patterns
from maploom.geonode.urls import urlpatterns as maploom_urls

urlpatterns = patterns('',
                       url(r'^$', 'geonode.views.index', dict(template='site_index.html'),  name='home'),
                       (r'^file-service/', include('geoshape.file_service.urls')),
                       (r'^proxy/', 'geoshape.views.proxy'),
                       )

urlpatterns += geonode_url_patterns
urlpatterns += maploom_urls

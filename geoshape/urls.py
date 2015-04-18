from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from geonode.urls import urlpatterns as geonode_url_patterns
from maploom.geonode.urls import urlpatterns as maploom_urls

urlpatterns = patterns('',
                       (r'^file-service/', include('geoshape.file_service.urls')),
                       (r'^proxy/', 'geoshape.views.proxy'),
                       url(r'^security/', TemplateView.as_view(template_name='security.html'), name='security'),
                       url(r'^about/api/', TemplateView.as_view(template_name='api.html'), name='about_api'),
                       ) 

urlpatterns += geonode_url_patterns
urlpatterns += maploom_urls

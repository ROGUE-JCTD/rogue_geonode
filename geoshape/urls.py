from django.conf.urls import patterns, include, url
from geonode.urls import urlpatterns as geonode_url_patterns
from geoshape.firestation.api import ResponseCapbabilityResource, FireStationResource
from maploom.geonode.urls import urlpatterns as maploom_urls
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(ResponseCapbabilityResource())
v1_api.register(FireStationResource())


urlpatterns = patterns('',
                       url(r'^$', 'geonode.views.index', dict(template='site_index.html'),  name='home'),
                       (r'^file-service/', include('geoshape.file_service.urls')),
                       (r'^proxy/', 'geoshape.views.proxy'),
                       (r'^jurisdictions/', include('geoshape.firestation.urls')),
                       (r'^api/', include(v1_api.urls)),
                       )

urlpatterns += geonode_url_patterns
urlpatterns += maploom_urls

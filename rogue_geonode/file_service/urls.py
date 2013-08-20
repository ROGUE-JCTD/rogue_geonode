from django.conf.urls import include, patterns, url

urlpatterns = patterns('',
    url(r'^(?P<key>[-\w\d\.]+?)$', 'rogue_geonode.file_service.views.index', name='file_service'),
    )

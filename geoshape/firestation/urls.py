from django.conf.urls import patterns, url
from .views import FireStationDetailView, ResponseCapabilityForm

urlpatterns = patterns('',
                       url(r'firestation/(?P<pk>\d+)/?$', FireStationDetailView.as_view(), name='firestation_detail'),
                       url(r'rc/?$', ResponseCapabilityForm.as_view(), name='response_capability_form'),
                       )


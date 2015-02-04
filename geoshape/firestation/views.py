from django.views.generic.edit import FormView
from django.views.generic import DetailView
from .forms import ResponseCapability
from .models import FireStation


class ResponseCapabilityForm(FormView):
    form_class = ResponseCapability
    template_name = 'firestation/response_capability.html'
    success_url = '/jurisdictions/rc'


class FireStationDetailView(DetailView):
    model = FireStation

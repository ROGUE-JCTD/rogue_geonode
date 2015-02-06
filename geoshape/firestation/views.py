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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FireStationDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        from django.forms.formsets import formset_factory
        context['formset'] = ResponseCapability
        return context

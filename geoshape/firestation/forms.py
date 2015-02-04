from django.forms import ModelForm, IntegerField
from .models import ResponseCapability


class ResponseCapability(ModelForm):

    class Meta:
        model = ResponseCapability
        exclude = ['firestation']
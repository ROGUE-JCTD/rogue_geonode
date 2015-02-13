import logging
from .models import FireStation, ResponseCapability
from tastypie import fields
from tastypie.authentication import SessionAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.cache import SimpleCache
from tastypie.contrib.gis.resources import ModelResource

logger = logging.getLogger(__name__)


# Note this is from one of my other projects, not sure it is actually needed or not.
class SessionAuth(SessionAuthentication):
    """
    This is a hack to fix a bug which returns occasional TypeErrors returned from SessionAuthentication.

    About:
    Every now and then the super class' get_identifier returns a TypeError (getattr(): attribute name must be string).
    It seems that the logic that returns the string used for the username sometimes returns None.

    """
    def get_identifier(self, request):
        """
        Provides a unique string identifier for the requestor.

        This implementation returns the user's username.
        """
        try:
            return super(SessionAuth, self).get_identifier(request)
        except TypeError:
            return getattr(request.user, 'username')


class FireStationResource(ModelResource):
    """
    The FireStation API.
    """

    class Meta:
        resource_name = 'firestations'
        queryset = FireStation.objects.all()
        authorization = DjangoAuthorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        cache = SimpleCache()


class ResponseCapbabilityResource(ModelResource):
    """
    The ResponseCapability API.
    """

    firestation = fields.ForeignKey(FireStationResource, 'firestation')

    class Meta:
        resource_name = 'capabilities'
        queryset = ResponseCapability.objects.all()
        authorization = DjangoAuthorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())

import httplib2
from django.contrib.auth import authenticate
from django.http import HttpResponse
from geonode.utils import _get_basic_auth_info
from logging import getLogger

logger = getLogger(__name__)

def index(request, key):
    redirect_url = "file-service/services/document/download?blobKey={0}".format(key)
    user = request.user
    logger.debug('User is authenticated: {0}'.format(user.is_authenticated()))
    logger.debug('Request.meta {0}'.format(request.META))
    if not user.is_authenticated() and 'HTTP_AUTHORIZATION' in request.META:

        try:
            username, password = _get_basic_auth_info(request)
            user = authenticate(username=username, password=password)
            logger.debug(user)
            logger.debug(user.is_authenticated())

        except Exception,e:
            logger.debug(e)

    if not user.is_authenticated():
        return HttpResponse('Unauthorized, please authenticate.', status=401)

    else:
        if request.method == 'GET':
            http = httplib2.Http()
            response, content = http.request(redirect_url, "GET", None)

            return HttpResponse(
                content=content,
                status=response.status,
                mimetype=response.get("content-type", "text/plain"))

        elif request.method == 'POST':
            raise NotImplemented

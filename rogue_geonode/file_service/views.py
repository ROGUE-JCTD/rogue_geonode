import httplib2
#import re
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from geonode.utils import _get_basic_auth_info
from logging import getLogger

logger = getLogger(__name__)


class BasicAuthView(View):
    """
    A mixin that requires the user to be logged in or logs in the user with basic auth, if the appropriate headers are
    present, before rendering the response.
    """

    unauthenticated_response = HttpResponse("Unauthorized, please authenticate.", status=401)

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        logger.debug(self.request)
        if not user.is_authenticated() and self.request.META.get('HTTP_AUTHORIZATION'):
            try:
                logger.debug("User is not logged in, but the request has basic auth headers.  Attempting to log "
                             "the user in.")
                username, password = _get_basic_auth_info(self.request)
                user = authenticate(username=username, password=password)
                logger.debug("Able to log user in: {0}".format(user.is_authenticated()))

            except Exception, e:
                logger.debug(e)
                return self.unauthenticated_response

        return self.unauthenticated_response if not user.is_authenticated() else \
            super(BasicAuthView, self).dispatch(*args, **kwargs)


class GetImage(BasicAuthView):
    """
    Proxies GET requests to the file-service application requiring authentication along the way.
    """
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        redirect_url = "http://127.0.0.1:8080/file-service/services/document/download?blobKey={0}".format(kwargs.get('key'))
        http = httplib2.Http()
        response, content = http.request(redirect_url, "GET")

        return HttpResponse(
            content=content,
            status=response.status,
            mimetype=response.get("content-type", "text/plain"))

class UploadImage(BasicAuthView):
    """
    Proxies POST requests to the file-service application requiring authentication along the way.
    """
    http_method_names = ['post']

    def post(self, *args, **kwargs):
        logger.debug('HERE')
        http = httplib2.Http()
        url = "http://127.0.0.1:8080/file-service/services/document/upload"
        #headers = dict(CONTENT_TYPE=self.request.META.get('CONTENT_TYPE', ''))
	#regex = re.compile('^HTTP_')
	#headers = dict((regex.sub('', header), value) for (header, value)
	#	in self.request.META.items() if header.startswith('HTTP_'))
	headers = dict((header, value) for header, value 
		in self.request.META.items() if header.startswith('HTTP_'))
	headers['CONTENT-TYPE'] = self.request.META.get('CONTENT_TYPE', '')
	headers['HOST'] = '127.0.0.1'
        response, content = http.request(url, body=self.request.body, method='POST', headers=headers)
        return HttpResponse(content=content, status=response.status, mimetype=response.get("content-type", "text/plain"))

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UploadImage, self).dispatch(*args, **kwargs)

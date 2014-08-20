import logging
from django.conf import settings
from django.http import HttpResponse
from django.http.request import validate_host
from django.utils.http import is_safe_url
from httplib import HTTPConnection
from urlparse import urlsplit
from geonode.geoserver.helpers import ogc_server_settings

logger = logging.getLogger(__name__)


def proxy(request):
    PROXY_ALLOWED_HOSTS = getattr(settings, 'PROXY_ALLOWED_HOSTS', ())
    hostname = (ogc_server_settings.hostname,) if ogc_server_settings else ()
    PROXY_ALLOWED_HOSTS += hostname

    if 'url' not in request.GET:
        return HttpResponse("The proxy service requires a URL-encoded URL as a parameter.",
                            status=400,
                            content_type="text/plain"
                            )

    raw_url = request.GET['url']
    url = urlsplit(raw_url)

    locator = url.path
    if url.query != "":
        locator += '?' + url.query
    if url.fragment != "":
        locator += '#' + url.fragment

    logger.debug('Incoming headers: {0}'.format(request.META))

    if not settings.DEBUG:
        if not validate_host(url.hostname, PROXY_ALLOWED_HOSTS):
            return HttpResponse("DEBUG is set to False but the host of the path provided "
                                "to the proxy service is not in the "
                                "PROXY_ALLOWED_HOSTS setting.",
                                status=403,
                                content_type="text/plain"
                                )
    headers = {}

    if settings.SESSION_COOKIE_NAME in request.COOKIES and is_safe_url(url=raw_url, host=ogc_server_settings.netloc):
        headers["Cookie"] = request.META["HTTP_COOKIE"]

    if request.META.get('HTTP_AUTHORIZATION'):
        headers['AUTHORIZATION'] = request.META.get('HTTP_AUTHORIZATION')

    if request.method in ("POST", "PUT") and "CONTENT_TYPE" in request.META:
        headers["Content-Type"] = request.META["CONTENT_TYPE"]

    if request.META.get('HTTP_ACCEPT'):
        headers['ACCEPT'] = request.META['HTTP_ACCEPT']

    logger.debug('Outgoing request method: {0}'.format(request.method))
    logger.debug('Outgoing request locator: {0}{1}'.format(url.hostname, locator))
    logger.debug('Outgoing request headers: {0}'.format(headers))

    conn = HTTPConnection(url.hostname, url.port)
    conn.request(request.method, locator, request.body, headers)
    result = conn.getresponse()

    logger.debug('Response headers: {0}'.format(result.getheaders()))
    logger.debug('Response status: {0}'.format(result.status))

    response = HttpResponse(result.read(),
                            status=result.status,
                            content_type=result.getheader("Content-Type", "text/plain"),
                            )

    if result.getheader('www-authenticate'):
        response['www-authenticate'] = "GeoNode"

    return response

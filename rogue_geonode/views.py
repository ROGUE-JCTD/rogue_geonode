import logging
from django.contrib.auth import authenticate
from django.conf import settings
from django.http import HttpResponse
from django.http.request import validate_host
from django.utils.http import is_safe_url
from django.utils.translation import ugettext as _
from django.utils import simplejson as json
from geonode.utils import _get_basic_auth_info
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
    conn.request(request.method, locator, request.raw_post_data, headers)
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


def resolve_user(request):

    user = None
    geoserver = False
    superuser = False
    acl_user = request.user
    if 'HTTP_AUTHORIZATION' in request.META:
        username, password = _get_basic_auth_info(request)
        acl_user = authenticate(username=username, password=password)
        if acl_user:
            user = acl_user.username
            superuser = acl_user.is_superuser
        elif _get_basic_auth_info(request) == ogc_server_settings.credentials:
            geoserver = True
            superuser = True
        else:
            return HttpResponse(_("Bad HTTP Authorization Credentials."),
                                status=401,
                                mimetype="text/plain")

    if not any([user, geoserver, superuser]) and not request.user.is_anonymous():
        user = request.user.username
        superuser = request.user.is_superuser

    resp = {
        'user': user,
        'geoserver': geoserver,
        'superuser': superuser,
    }

    if acl_user and acl_user.is_authenticated():
        resp['fullname'] = acl_user.profile.name
        resp['email'] = acl_user.profile.email
    return HttpResponse(json.dumps(resp))

from django.conf import settings
from django.utils.translation import ugettext as _
from geoshape.version import get_version


def security_warnings(request, PROXY_ALLOWED_HOSTS=()):
    """ Detects insecure settings and reports them to the client-side context. """

    warnings = []

    PROXY_ALLOWED_HOSTS = PROXY_ALLOWED_HOSTS or getattr(settings, 'PROXY_ALLOWED_HOSTS', ())

    if PROXY_ALLOWED_HOSTS and '*' in PROXY_ALLOWED_HOSTS:
        warnings.append(dict(title=_('Insecure setting detected.'),
                             description=_('A wildcard is included in the PROXY_ALLOWED_HOSTS setting.')))

    return dict(warnings=warnings)


def rogue(request):
    """ Returns the geoshape version """

    return dict(VERSION=get_version())


def fileservice(request):
    """ Returns url template that can be used by client to resolve path to endpoint that serves media """

    conf = getattr(settings, 'FILESERVICE_CONFIG', {})
    return dict(fileservice_url_template=conf.get('url_template', '/api/fileservice/{}/view'))

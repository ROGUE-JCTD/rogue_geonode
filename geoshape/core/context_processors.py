from django.conf import settings
from django.utils.translation import ugettext as _
from geoshape.version import get_version


def security_statements(request):
    """ Pass SECURITY_STATEMENTS from settings for security.html template. """

    return dict(SECURITY_STATEMENTS=getattr(settings, 'SECURITY_STATEMENTS', None))


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

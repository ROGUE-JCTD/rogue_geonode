from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from geoshape.core.context_processors import security_warnings
from lxml import etree

import logging
logger = logging.getLogger(__name__)

User = get_user_model()


class ROGUETests(TestCase):

    def setUp(self):
        self.username = 'admin'
        self.password = 'admin'
        self.user, created = User.objects.get_or_create(username=self.username, is_superuser=True)

        if created:
            self.user.set_password(self.password)
            self.user.save()

    def test_jpeg_decoder(self):
        """
        Ensure the jpeg decoder is installed.

        The jpeg decoder (libjpeg) is a django-avatar dependency that can be installed with your operating system's
        package installer.  This test case fails if the decoder is not installed.
        """

        try:
            from PIL.Image import core
            getattr(core, "jpeg_decoder")
        except IOError:
            self.fail("JPEG Decoder not installed.")
        except ImportError:
            pass

    @staticmethod
    def get_elements_from_xpath(content, xpath='//title'):
        html = etree.HTML(content)
        return html.xpath(xpath)

    def test_security_warnings(self):
        """
        Tests the security warnings context processor.
        """

        PROXY_ALLOWED_HOSTS = ('*',)
        warnings = security_warnings(None, PROXY_ALLOWED_HOSTS)
        self.assertDictEqual(warnings, {'warnings': [{'description': u'A wildcard is included in '
                                                                     u'the PROXY_ALLOWED_HOSTS setting.',
                                                      'title': u'Insecure setting detected.'}]})

        PROXY_ALLOWED_HOSTS = ('.openstreetmap.com',)
        warnings = security_warnings(None, PROXY_ALLOWED_HOSTS)
        self.assertDictEqual(warnings, {'warnings': []})

    def test_documentation_links(self):
        """
        Ensures that links to the documentation are included in the templates.
        """

        c = Client()
        c.login(username=self.username, password=self.password)
        resp = c.get(reverse('home'), follow=True)
        docs_links = self.get_elements_from_xpath(resp.content, xpath='//a[@href="/docs"]')
        self.assertTrue(len(docs_links) > 0)

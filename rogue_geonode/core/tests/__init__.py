from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from django.test.utils import override_settings
from rogue_geonode.core.context_processors import security_warnings
from lxml import etree

import logging
logger = logging.getLogger(__name__)


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

    def test_overridden_title(self):
        """
        Test to ensure there are no regressions for https://github.com/ROGUE-JCTD/rogue_geonode/issues/9.
        """

        c = Client()
        c.login(username=self.username, password=self.password)

        custom_views = ['layer_browse', 'documents_browse', 'maps_browse', 'profile_browse']

        for template in custom_views:
            resp = c.get(reverse(template), follow=True)
            title = self.get_elements_from_xpath(resp.content)
            self.assertTrue(title, msg="The page has no title element!")
            self.assertNotIn('Explore', title[0].text)

            page_title = self.get_elements_from_xpath(resp.content, xpath="//*[contains(@class, 'page-title')]")
            self.assertTrue(page_title, msg="The page has no page-title element!")

            self.assertNotIn('Explore',
                             page_title[0].text,
                             msg="'Explore' was found in the {} template.".format(template))

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



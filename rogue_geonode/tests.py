from django.test import Client, TestCase


class ROGUETests(TestCase):

    def test_jpeg_decoder(self):
        """
        Ensure the jpeg decoder is installed.

        The jpeg decoder (libjpeg) is a django-avatar dependency that can be installed with your operating system's
        package installer.  This test case fails if the decoder is not installed.
        """

        try:
            from PIL.Image import core
            decoder = getattr(core, "jpeg_decoder")
        except IOError:
            self.fail("JPEG Decoder not installed.")
        except ImportError:
            pass








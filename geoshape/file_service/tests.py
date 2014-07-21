"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class SimpleTest(TestCase):

    def setUp(self):
        user, created = User.objects.get_or_create(username='test_admin',
                                                   password='admin',
                                                   is_active=True)

        user.set_password('admin')
        user.save()

        self.user = user

    def test_index(self):
        """
        Test for the main view.
        """

        c = Client()
        response = c.get(reverse('file_service', kwargs=dict(key='test')))

        # Non-authenticated user should return 401
        self.assertEqual(response.status_code, 401)

        logged_in = c.login(username='test_admin', password='admin')
        self.assertTrue(logged_in)

        # An authenticated user should return a 200
        response = c.get(reverse('file_service', kwargs=dict(key='test')))
        self.assertEqual(response.status_code, 200)

        c.logout()

        # A client should get a 200 response with basic authorization
        headers = dict(HTTP_AUTHORIZATION="basic dGVzdF9hZG1pbjphZG1pbg==")
        response = c.get(reverse('file_service', kwargs=dict(key='test')), **headers)
        self.assertEqual(response.status_code, 200)

        # A client should get a 401 response with incorrect basic authorization
        headers = dict(HTTP_AUTHORIZATION="basic dGasdasdsabg==")
        response = c.get(reverse('file_service', kwargs=dict(key='test')), **headers)
        self.assertEqual(response.status_code, 401)
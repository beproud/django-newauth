#:coding=utf-8:
from urllib.parse import urlparse

import pytest
from django.test import TestCase as DjangoTestCase
from django.conf import settings

__all__ = (
    'DecoratorTest',
)


@pytest.mark.django_db
class DecoratorTest(DjangoTestCase):
    fixtures = ['authutils_testdata.json']

    def test_login_required_failed(self):
        response = self.client.get("/testapp/login_required/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.get("Location", ""))[2], settings.LOGIN_URL)

    def test_login_required_testapp_failed(self):
        response = self.client.get("/testapp/testapp_login_required/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.get("Location", ""))[2], settings.LOGIN_URL)

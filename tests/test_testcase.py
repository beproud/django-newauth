#:coding=utf-8:

import pytest
from django.test import TestCase as DjangoTestCase

from newauth.test import AuthTestCaseMixin
from base import BaseTestCase


@pytest.mark.django_db
class AuthTestCaseMixinTest(BaseTestCase, AuthTestCaseMixin, DjangoTestCase):
    fixtures = ['authutils_testdata.json']

    def test_auth_login(self):
        self.auth_login(user_id=1)
        self.assertEqual(self.client.session['_newauth_user']['uid'], 1)

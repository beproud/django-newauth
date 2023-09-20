#:coding=utf-8:

import pytest
from django.test import TestCase as DjangoTestCase
from django import http
from django.http import HttpResponse
from django.contrib.sessions.middleware import SessionMiddleware

from newauth.constants import DEFAULT_USER_PROPERTY
from newauth.middleware import AuthMiddleware


def get_response_empty(request):
    return HttpResponse()


@pytest.mark.django_db
class MiddlewareTest(DjangoTestCase):
    fixtures = ['authutils_testdata.json']

    def setUp(self):
        self.middleware = AuthMiddleware(get_response_empty)
        self.session_middleware = SessionMiddleware(get_response_empty)

    def test_process_request(self):
        request = http.HttpRequest()
        self.session_middleware.process_request(request)

        request.session['_newauth_user'] = {'uid': 1, 'bn': 'testapp2'}
        self.middleware.process_request(request)

        self.assertTrue(getattr(request, DEFAULT_USER_PROPERTY, None).is_authenticated(),
                "Auth user not authenticated")

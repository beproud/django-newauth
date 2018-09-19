#:coding=utf-8:
import mock
from django.utils.six.moves.urllib_parse import quote
from django.test import TestCase as DjangoTestCase
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.conf import settings
from django.http import HttpResponse

from testapp.models import TestBasicUser


class LoginViewsTest(DjangoTestCase):
    fixtures = ['authutils_testdata.json']

    def setUp(self):
        TestBasicUser.objects.create_user(
            username="testuser",
            password="password",
        )

    def test_login(self):
        # Need to do a get first to for the cookie test.
        self.assertContains(self.client.get('/account/login/'), '<form')
        response = self.client.post('/account/login/', {
            'username': 'testuser',
            'password': 'password',
        })
        self.assertEquals(response.status_code, 302)
        self.assertTrue(response['Location'].endswith(settings.LOGIN_REDIRECT_URL))

    def test_login_override_redirect_url(self):
        redirect_url = 'test_login_redirect_url/'
        with self.settings(LOGIN_REDIRECT_URL=redirect_url):
            self.assertContains(self.client.get('/account/login/'), '<form')
            response = self.client.post('/account/login/', {
                'username': 'testuser',
                'password': 'password',
            })
        self.assertEquals(response.status_code, 302)
        self.assertTrue(response['Location'].endswith(redirect_url))

    def test_fail_login(self):
        response = self.client.post('/account/login/', {
            'username': 'testclient',
            'password': 'bad_password',
        })
        self.assertEquals(response.status_code, 200)
        self.assertFormError(response, 'form', None, "Please enter a correct username and password. Note that both fields may be case-sensitive.")

    def test_fail_login_blank_fields(self):
        # blank username
        response = self.client.post('/account/login/', {
            'username': '',
            'password': 'password',
        })
        self.assertEquals(response.status_code, 200)
        self.assertFormError(response, 'form', 'username', u'This field is required.')

        # blank password
        response = self.client.post('/account/login/', {
            'username': 'testuser',
            'password': '',
        })
        self.assertEquals(response.status_code, 200)
        self.assertFormError(response, 'form', 'password', u'This field is required.')

    def test_bad_redirect_space(self):
        bad_next_url = 'test space url'
        self.assertContains(self.client.get('/account/login/'), '<form')
        response = self.client.post('/account/login/', {
            'username': 'testuser',
            'password': 'password',
            REDIRECT_FIELD_NAME: bad_next_url,
        })
        self.assertEquals(response.status_code, 302)
        self.assertTrue(response['Location'].endswith(settings.LOGIN_REDIRECT_URL))

    def test_bad_redirect_empty(self):
        bad_next_url = ''
        self.assertContains(self.client.get('/account/login/'), '<form')
        response = self.client.post('/account/login/', {
            'username': 'testuser',
            'password': 'password',
            REDIRECT_FIELD_NAME: bad_next_url,
        })
        self.assertEquals(response.status_code, 302)
        self.assertTrue(response['Location'].endswith(settings.LOGIN_REDIRECT_URL))

    def test_bad_redirect_domain(self):
        bad_next_url = 'http://example.com/'
        self.assertContains(self.client.get('/account/login/'), '<form')
        with self.settings(ALLOWED_HOSTS=['django-newauth.com']):
            response = self.client.post('/account/login/', {
                'username': 'testuser',
                'password': 'password',
                REDIRECT_FIELD_NAME: bad_next_url,
            }, HTTP_HOST='django-newauth.com')
        self.assertEquals(response.status_code, 302)
        self.assertTrue(response['Location'].endswith(settings.LOGIN_REDIRECT_URL))

    def test_bad_redirect_domain_other_case(self):
        bad_next_url = 'http://example2.com/'
        self.assertContains(self.client.get('/account/login/'), '<form')
        with self.settings(ALLOWED_HOSTS=['example.com']):
            response = self.client.post('/account/login/', {
                'username': 'testuser',
                'password': 'password',
                REDIRECT_FIELD_NAME: bad_next_url,
            }, HTTP_HOST='example.com')
        self.assertEquals(response.status_code, 302)
        self.assertTrue(response['Location'].endswith(settings.LOGIN_REDIRECT_URL))

    def test_ok_redirect_domain(self):
        next_url = 'http://django-newauth.com/path/to/resource/'
        self.assertContains(
            self.client.get('/account/login/'), '<form')
        with self.settings(ALLOWED_HOSTS=['django-newauth.com']):
            response = self.client.post('/account/login/', {
                'username': 'testuser',
                'password': 'password',
                REDIRECT_FIELD_NAME: next_url,
            }, HTTP_HOST='django-newauth.com')
        self.assertEquals(response.status_code, 302)
        self.assertTrue(response['Location'].endswith(next_url))

    def test_ok_redirect_domain_as_parameter(self):
        ok_url = '/some/url?param=http://example.com/'
        self.assertContains(self.client.get('/account/login/'), '<form')
        with self.settings(ALLOWED_HOSTS=['django-newauth.com']):
            response = self.client.post('/account/login/', {
                'username': 'testuser',
                'password': 'password',
                REDIRECT_FIELD_NAME: ok_url,
            }, HTTP_HOST='django-newauth.com')
        self.assertEquals(response.status_code, 302)
        self.assertTrue(response['Location'].endswith('/some/url?param=http://example.com/'))

    def test_ok_redirect(self):
        ok_url = '/path/to/resource/'
        self.assertContains(self.client.get('/account/login/'), '<form')
        response = self.client.post('/account/login/', {
            'username': 'testuser',
            'password': 'password',
            REDIRECT_FIELD_NAME: ok_url,
        })
        self.assertEquals(response.status_code, 302)
        self.assertTrue(response['Location'].endswith(ok_url))


class LogoutViewsTest(DjangoTestCase):
    fixtures = ['authutils_testdata.json']

    def test_get_logout_default(self):
        """
        logout with HTTP GET
        default LOGOUT_render_URL settings
        """
        response = self.client.get('/account/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Logged out page')

    def test_post_logout_default(self):
        """
        logout with HTTP POST
        default LOGOUT_render_URL settings
        """
        response = self.client.post('/account/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Logged out page')

    def test_logout_override_settings(self):
        """
        logout with HTTP POST
        override LOGOUT_REDIRECT_URL settings
        """
        redirect_url = '/path/to/redirect/'
        with self.settings(LOGOUT_REDIRECT_URL=redirect_url):
            response = self.client.post('/account/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response['Location'].endswith(redirect_url))

    def test_logout_to_redirect(self):
        """
        logout with HTTP POST
        redirect to set redirct_url
        """
        redirect_url = '/path/to/resource/'
        response = self.client.post('/account/logout/', {REDIRECT_FIELD_NAME: redirect_url})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response['Location'].endswith(redirect_url))

    def test_get_logout_to_bad_redirect(self):
        """
        logout with HTTP GET, defend open redirect.
        """
        redirect_url = 'http://example.com/path/to/resource/'
        response = self.client.get('/account/logout/?%s=%s' % (REDIRECT_FIELD_NAME, quote(redirect_url)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Logged out page')

    def test_get_logout_to_ok_redirect(self):
        """
        logout with HTTP GET, ok redirect.
        """
        redirect_url = 'http://django-newauth.com/path/to/resource/'
        with self.settings(ALLOWED_HOSTS=['django-newauth.com']):
            response = self.client.get(
                '/account/logout/?%s=%s' % (REDIRECT_FIELD_NAME, quote(redirect_url)),
                HTTP_HOST='django-newauth.com',
            )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response['Location'].endswith(redirect_url))

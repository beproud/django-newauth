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
        super(LoginViewsTest, self).setUp()
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
        response = self.client.post('/account/login/', {
            'username': 'testuser',
            'password': 'password',
            REDIRECT_FIELD_NAME: bad_next_url,
        })
        self.assertEquals(response.status_code, 302)
        self.assertTrue(response['Location'].endswith(settings.LOGIN_REDIRECT_URL))

    def test_ok_redirect_domain(self):
        ok_url = '/some/url?param=http://example.com/'
        self.assertContains(self.client.get('/account/login/'), '<form')
        response = self.client.post('/account/login/', {
            'username': 'testuser',
            'password': 'password',
            REDIRECT_FIELD_NAME: ok_url,
        })
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

    @mock.patch('newauth.views.render')
    def test_get_logout_default(self, mock_render):
        """
        logout with HTTP GET
        default LOGOUT_render_URL settings
        """
        mock_render.return_value = HttpResponse('logged out')
        self.client.get('/account/logout/')
        mock_render.assert_called()

    @mock.patch('newauth.views.render')
    def test_post_logout_default(self, mock_render):
        """
        logout with HTTP POST
        default LOGOUT_render_URL settings
        """
        mock_render.return_value = HttpResponse('logged out')
        self.client.post('/account/logout/')
        mock_render.assert_called()

    @mock.patch('newauth.views.redirect')
    def test_logout_override_settings(self, mock_redirect):
        """
        logout with HTTP POST
        override LOGOUT_REDIRECT_URL settings
        """
        mock_redirect.return_value = HttpResponse('logged out')
        redirect_url = '/path/to/redirect/'
        with self.settings(LOGOUT_REDIRECT_URL=redirect_url):
            self.client.post('/account/logout/')
        mock_redirect.assert_called_once_with(redirect_url)

    @mock.patch('newauth.views.redirect')
    def test_logout_to_redirect(self, mock_redirect):
        """
        logout with HTTP POST
        redirect to set redirct_url
        """
        mock_redirect.return_value = HttpResponse('logged out')
        redirect_url = '/path/to/resource/'
        self.client.post('/account/logout/', {REDIRECT_FIELD_NAME: redirect_url})
        mock_redirect.assert_called_once_with(redirect_url)

    @mock.patch('newauth.views.render')
    def test_get_logout_to_bad_redirect(self, mock_render):
        """
        logout with HTTP GET, defend open redirect.
        """
        mock_render.return_value = HttpResponse('logged out')
        redirect_url = 'http://example.com/path/to/resource/'
        self.client.get('/account/logout/?%s=%s' % (REDIRECT_FIELD_NAME, quote(redirect_url)))
        mock_render.assert_called()

    @mock.patch('newauth.views.render')
    def test_post_logout_to_bad_redirect(self, mock_render):
        """
        logout with HTTP POST, defend open redirect.
        """
        mock_render.return_value = HttpResponse('logged out')
        redirect_url = 'http://example.com/path/to/resource/'
        self.client.post('/account/logout/', {REDIRECT_FIELD_NAME: redirect_url})
        mock_render.assert_called()

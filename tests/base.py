#:coding=utf-8:

import os

from django.conf import settings

from newauth import api as auth_api

AVAILABLE_SETTINGS = (
    'MIDDLEWARE_CLASSES',
    'NEWAUTH_BACKENDS',
    'NEWAUTH_USER_MODELS',
    'NEWAUTH_USER_PROPERTY',
    'NEWAUTH_SESSION_KEY',
    'NEWAUTH_PASSWORD_ALGO',
    'TEMPLATE_DIRS',
)


class BaseTestCase(object):
    NEWAUTH_BACKENDS = {
        'default': {
            'backend': 'newauth.backend.BasicUserBackend',
            'user': 'testapp.models.TestBasicUser',
            'anon_user': 'newauth.api.BasicAnonymousUser',
        },
        'testapp': {
            'backend': (
                'testapp.backends.TestBackend',
                'testapp.backends.TestBackend3',
            ),
            'user': 'testapp.models.TestUser',
            'anon_user': 'newauth.api.BasicAnonymousUser',
        },
        'testapp2': {
            'backend': 'testapp.backends.TestBackend2',
            'user': 'testapp.models.TestUser',
            'anon_user': 'newauth.api.BasicAnonymousUser',
        },
        'testapp3': {
            'backend': 'testapp.backends.TestBackend3',
            'user': 'testapp.models.TestUser3',
            'anon_user': 'testapp.models.TestAnonymousUser3',
        }
    }

    TEMPLATE_DIRS = (
        os.path.join(os.path.dirname(__file__), 'templates'),
    )

    def setUp(self):
        # Clear the backend cache so it's reloaded in case the
        # settings have changed
        auth_api._auth_backend_cache = {}

        for setting_name in AVAILABLE_SETTINGS:
            setting_value = getattr(self, setting_name, None)
            setattr(self, "_old_"+setting_name, getattr(settings, setting_name, None))
            if setting_value:
                setattr(settings, setting_name, setting_value)

    def tearDown(self):
        for setting_name in AVAILABLE_SETTINGS:
            old_setting_value = getattr(self, "_old_"+setting_name, None)
            if old_setting_value is None:
                if hasattr(settings, setting_name):
                    delattr(settings, setting_name)
            else:
                setattr(settings, setting_name, old_setting_value)

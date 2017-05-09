# -*- coding: utf-8 -*-
import os
from django import VERSION as DJANGO_VERSION

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'newauth',
    'testapp',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test',
    }
}
ROOT_URLCONF='testapp.urls'
MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'newauth.middleware.AuthMiddleware',
)
if DJANGO_VERSION < (1, 9):
    MIDDLEWARE_CLASSES = MIDDLEWARE
TEMPLATES=[{
    'DIRS': [os.path.join(os.path.dirname(__file__), 'templates')],
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
}]
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
SECRET_KEY = '<key>'

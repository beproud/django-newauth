# -*- coding: utf-8 -*-
import os

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
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'newauth.middleware.AuthMiddleware',
)
TEMPLATES=[{
    'DIRS': [os.path.join(os.path.dirname(__file__), 'templates')],
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
}]
NEWAUTH_BACKENDS = {
    'default': {
        'backend': 'newauth.backend.BasicUserBackend',
        'user': 'testapp.models.TestBasicUser',
        'anon_user': 'newauth.api.BasicAnonymousUser',
    }
}
SECRET_KEY = '<key>'

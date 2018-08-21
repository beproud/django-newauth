# :coding=utf-8:

from django.dispatch import Signal

#: This is notification by Django signals format, send after a logged in.
user_logged_in = Signal(providing_args=['request', 'user'])

#: This is notification by Django signals format, send after a logged out.
user_logged_out = Signal(providing_args=['request', 'user'])

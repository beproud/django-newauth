=========
ChangeLog
=========

Release 0.40 (2021-12-28)
=========================

- Support Django-3.2
- Support Python-3.7, 3.8, 3.9, 3.10
- Drop Django-1.11, 3.1
- Drop Python-2.7

Release 0.39 (2020-04-30)
=========================

- Fixed: If login_required is used with Python3, login authentication after the second time fails.
- Support Django-2.2
- Drop Django-1.10

Release 0.38 (2018-09-20)
=========================

- Add missing classifiers: py36, dj versions.
- provide universal wheel
- Add feature: send logged in signal & logged out signal
- Security: masking sensitive post parameter
- Security: safe redirect url for open redirect possibility
- Security: strict safety check for redirect url 

Release 0.37 (2017-05-15)
=========================

- Support Python-3.6
- Support Django-1.11
- Drop Django-1.9

Release 0.36 (2016-12-14)
=========================

- Fixed: issue #7 Exception Type: AttributeError at /logout/


Release 0.35 (2016-11-30)
=========================

- 'newauth.middleware.AuthMiddleware' supports ``settings.MIDDLEWARE`` since django-1.10

Release 0.34 (2016-11-25)
=========================

- Support Django-1.10
- Drop Django-1.7 or earlier
- Provide documentation on ReadTheDocs: http://django-newauth.rtfd.io/

Release 0.33 (2016-02-01)
=========================

- More support Django-1.8 & 1.9

Release 0.32 (2016-01-19)
=========================

- Support Django-1.8 & 1.9


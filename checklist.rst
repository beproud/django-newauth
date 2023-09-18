.. release procedure

Procedure:

1. check CI status testing result: https://github.com/beproud/django-newauth/actions
2. update release version/date in ``ChangeLog.rst``
3. run ``python -m build``
4. check ``twine check dist/*``
5. upload ``twine upload dist/*``
6. tagging version e.g. ``git tag 0.40``.
7. check PyPI page: https://pypi.org/p/django-newauth
8. bump versions and commit/push them onto GitHub

   * ``ChangeLog.rst``  next version
   * ``newauth/__init__.py`` next version

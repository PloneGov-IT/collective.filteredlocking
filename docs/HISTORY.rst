Changelog
=========

2.0.1 (unreleased)
------------------

- Nothing changed yet.


2.0.0 (2022-07-15)
------------------

- Python 3 support. Dropped support for Python 2.7 and Plone < 5.2.
  [reflab]


1.2.0 (2014-05-15)
------------------

- Fix to egg format [keul]
- Proper package dependencies [keul]
- Removed useless GS profiles [keul]
- Do not rewrite the whole ``TTWLockable`` code, but inherit from Plone default ones [keul]
- Pyflakes cleanup [keul]
- Default permission will now replicate default Plone behavior (edit can release locks) [keul]
- A user can always remove his own lock. This prevent strange behavior where users lockout
  others because they don't have the proper permission [keul]
- Added support for Site Administrator role [keul]
- Added tests suite

1.1.0 (2013-06-24)
------------------

* z3c.autoinclude

1.0.0 - Unreleased
------------------

* Initial release


# -*- coding: utf-8 -*-

from zope.configuration import xmlconfig

from plone.testing import z2

from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID


class FilteredLockingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.filteredlocking
        xmlconfig.file('configure.zcml',
                       collective.filteredlocking,
                       context=configurationContext)
        z2.installProduct(app, 'collective.filteredlocking')

    def setUpPloneSite(self, portal):
        setRoles(portal, TEST_USER_ID, ['Member', 'Manager'])
        acl_users = portal.acl_users
        acl_users.userFolderAddUser('user1', 'secret', ['Member'], [])
        setRoles(portal, 'user1', ['Member', 'Editor', ])
        acl_users.userFolderAddUser('user2', 'secret', ['Member'], [])
        setRoles(portal, 'user2', ['Member', 'Editor', ])


FILTERED_LOCKING_FIXTURE = FilteredLockingLayer()
FILTERED_LOCKING_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(FILTERED_LOCKING_FIXTURE, ),
                       name="FilteredLocking:Integration")
FILTERED_LOCKING_FUNCTIONAL_TESTING = \
    FunctionalTesting(bases=(FILTERED_LOCKING_FIXTURE, ),
                       name="FilteredLocking:Functional")


# -*- coding: utf-8 -*-

from Products.CMFCore.permissions import setDefaultRoles
from AccessControl import ModuleSecurityInfo

security = ModuleSecurityInfo("collective.filteredlocking")

PROJECTNAME = 'collective.filteredlocking'

#permission to unlock locked objects
security.declarePublic("CanUnlockObjects")
CanUnlockObjects = "collective.filteredlocking: Can unlock objects"
setDefaultRoles(CanUnlockObjects, ('Manager','Owner'))
   
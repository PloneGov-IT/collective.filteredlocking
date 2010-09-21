# -*- coding: utf-8 -*-

from Products.CMFCore.permissions import setDefaultRoles
from AccessControl import ModuleSecurityInfo

security = ModuleSecurityInfo("rer.filteredlocking")

PROJECTNAME = 'rer.filteredlocking'

#permission to unlock locked objects
security.declarePublic("CanUnlockObjects")
CanUnlockObjects = "rer.filteredlocking: Can unlock objects"
setDefaultRoles(CanUnlockObjects, ('Manager','Owner'))
   
# -*- coding: utf-8 -*-

from collective.filteredlocking import config
from plone.locking.interfaces import STEALABLE_LOCK
from plone.locking.lockable import TTWLockable


class FilteredTTWLockable(TTWLockable):
    """An object that is being locked through-the-web
    """

    def stealable(self, lock_type=STEALABLE_LOCK):
        if not self._user_can_unlock():
            return False
        return super(FilteredTTWLockable, self).stealable(lock_type)
    
    def _user_can_unlock(self):
        pm=getToolByName(self.context,'portal_membership')
        user=pm.getAuthenticatedMember()
        return user.checkPermission(config.CanUnlockObjects, self.context)

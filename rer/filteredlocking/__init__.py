# -*- coding: utf-8 -*-
import config

from zope.i18nmessageid import MessageFactory

filteredlockingMessageFactory = MessageFactory('rer.filteredlocking')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

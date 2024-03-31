"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "prova_utfpr"

_ = MessageFactory("prova_utfpr")

logger = logging.getLogger("prova_utfpr")

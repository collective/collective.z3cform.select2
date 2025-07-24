# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from z3c.form.interfaces import IFormLayer
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveZ3CformSelect2Layer(IFormLayer, IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

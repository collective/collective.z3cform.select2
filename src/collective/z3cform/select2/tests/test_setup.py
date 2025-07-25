# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.z3cform.select2.testing import COLLECTIVE_Z3CFORM_SELECT2_INTEGRATION_TESTING  # noqa
from plone.base.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.z3cform.select2 is properly installed."""

    layer = COLLECTIVE_Z3CFORM_SELECT2_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal)

    def test_product_installed(self):
        """Test if collective.z3cform.select2 is installed."""
        self.assertTrue(
            self.installer.is_product_installed("collective.z3cform.select2")
        )

    def test_browserlayer(self):
        """Test that ICollectiveZ3CformSelect2Layer is registered."""
        from collective.z3cform.select2.interfaces import ICollectiveZ3CformSelect2Layer
        from plone.browserlayer import utils

        self.assertIn(ICollectiveZ3CformSelect2Layer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_Z3CFORM_SELECT2_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal)
        self.installer.uninstall_product("collective.z3cform.select2")

    def test_product_uninstalled(self):
        """Test if collective.z3cform.select2 is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("collective.z3cform.select2")
        )

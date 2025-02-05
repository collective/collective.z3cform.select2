# -*- coding: utf-8 -*-

import unittest
import z3c.form.term
import zope.component
import zope.schema.interfaces
from collective.z3cform.select2.widget.widget import SingleSelect2Widget
from collective.z3cform.select2.widget.widget import MultiSelect2Widget
from collective.z3cform.select2.widget.widget import ISingleSelect2Widget
from collective.z3cform.select2.widget.widget import IMultiSelect2Widget

from collective.z3cform.select2.testing import COLLECTIVE_Z3CFORM_SELECT2_INTEGRATION_TESTING  # noqa
from z3c.form.interfaces import IFormLayer
from z3c.form.testing import getPath
from z3c.form.testing import TestRequest
from z3c.form.widget import WidgetTemplateFactory
from zope.pagetemplate.interfaces import IPageTemplate
from zope.schema.vocabulary import SimpleVocabulary


class SelectionTerms(z3c.form.term.Terms):
    def __init__(self, context, request, form, field, widget):
        self.terms = SimpleVocabulary.fromValues(['a', 'b', 'c'])


class TestSingleSelect2Widget(unittest.TestCase):
    """Test the SingleSelect2Widget."""

    layer = COLLECTIVE_Z3CFORM_SELECT2_INTEGRATION_TESTING

    def test_widget(self):
        """ """
        request = TestRequest()
        widget = SingleSelect2Widget(request)
        # we need correct id and name for rendering
        widget.id = 'widget-id'
        widget.name = 'widget.name'
        # we also need to register the template for the widget and request
        zope.component.provideAdapter(
            WidgetTemplateFactory(getPath('select_input.pt'), 'text/html'),
            (None, None, None, None, ISingleSelect2Widget),
            IPageTemplate, name='input')
        self.assertEqual(
            widget.render(),
            '\n<select id="widget_id" name="widget.name:list" '
            'class="single-select2-widget" readonly="" accesskey="" '
            'size="1">\n\n</select>\n\n')

        # provide a vocabulary. We can do this by defining a source providing
        # ``ITerms``. This source uses descriminators which will fit our setup.
        zope.component.provideAdapter(
            SelectionTerms,
            (None, IFormLayer, None, None, ISingleSelect2Widget))
        widget.update()
        self.assertEqual(
            widget.render(),
            '\n<select id="widget_id" name="widget.name:list" class="'
            'single-select2-widget" readonly="" '
            'accesskey="" size="1">\n'
            '<option id="widget-id-novalue" value="--NOVALUE--" '
            'selected="selected" data-css="--NOVALUE--">No value</option\n   >'
            '<option id="widget-id-0" value="a" data-css="a">a</option\n >'
            '<option id="widget-id-1" value="b" data-css="b">b</option\n >'
            '<option id="widget-id-2" value="c" data-css="c">c</option\n >\n'
            '</select>\n\n')


class TestMultiSelect2Widget(unittest.TestCase):
    """Test the MultiSelect2Widget."""

    layer = COLLECTIVE_Z3CFORM_SELECT2_INTEGRATION_TESTING

    def test_widget(self):
        """ """
        request = TestRequest()
        widget = MultiSelect2Widget(request)
        # we need correct id and name for rendering
        widget.id = 'widget-id'
        widget.name = 'widget.name'
        # we also need to register the template for the widget and request
        zope.component.provideAdapter(
            WidgetTemplateFactory(getPath('select_input.pt'), 'text/html'),
            (None, None, None, None, IMultiSelect2Widget),
            IPageTemplate, name='input')
        self.assertEqual(
            widget.render(),
            '\n<select id="widget_id" name="widget.name:list" '
            'class="multi-select2-widget" readonly="" accesskey="" '
            'multiple="" size="1">\n\n</select>\n\n')

        # provide a vocabulary. We can do this by defining a source providing
        # ``ITerms``. This source uses descriminators which will fit our setup.
        zope.component.provideAdapter(
            SelectionTerms,
            (None, IFormLayer, None, None, IMultiSelect2Widget))
        widget.update()
        self.assertEqual(
            widget.render(),
            '\n<select id="widget_id" name="widget.name:list" class="'
            'multi-select2-widget" readonly="" '
            'accesskey="" multiple="" size="1">\n'
            '<option id="widget-id-0" value="a" data-css="a">a</option\n >'
            '<option id="widget-id-1" value="b" data-css="b">b</option\n >'
            '<option id="widget-id-2" value="c" data-css="c">c</option\n >\n'
            '</select>\n\n')

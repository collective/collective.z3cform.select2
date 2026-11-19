# -*- coding: utf-8 -*-
"""Installer for the collective.z3cform.select2 package."""

from setuptools import setup


long_description = (
    open("README.rst").read()
    + "\n"
    + "Contributors\n"
    + "============\n"
    + "\n"
    + open("CONTRIBUTORS.rst").read()
    + "\n"
    + open("CHANGES.rst").read()
    + "\n"
)


setup(
    name="collective.z3cform.select2",
    version="4.0.1.dev0",
    description="select2 widget for z3c.form and eea.facetednavigation",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.13",
    ],
    keywords="Python Plone",
    author="Vincent Fretin",
    author_email="vincent.fretin@gmail.com",
    url="https://pypi.python.org/pypi/collective.z3cform.select2",
    license="GPL version 2",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "plone.api",
        "eea.facetednavigation",
        "z3c.form",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
        ],
    },
    entry_points="""
    """,
)

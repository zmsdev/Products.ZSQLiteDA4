##############################################################################
#
# Copyright (c) 2009-2020 Hajime Nakagami and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import os

from setuptools import find_packages
from setuptools import setup


NAME = 'Products.ZSQLiteDA'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(name=NAME,
      version=read('version.txt').strip(),
      description='The ZSQLiteDA product provides support for SQLite database adapter objects in Zope.',
      long_description=read('README.md'),
      classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Web Environment",
        "Framework :: Zope",
        "Framework :: Zope :: 4",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development",
        "Topic :: System :: Systems Administration ::"
        ],
      keywords='web application server zope database adapter sqlite',
      author="Hajime Nakagami and contributors",
      author_email="info@zms-publishing.com",
      url="https://github.com/zmsdev/%s" % NAME,
      project_urls={
        'Documentation': 'https://productsldapuserfolder.readthedocs.io/',
        'Issue Tracker': 'https://github.com/dataflake/%s/issues' % NAME,
        'Sources': 'https://github.com/dataflake/%s' % NAME,
      },
      python_requires='>=3.6',
      license="ZPL 2.1",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['Products'],
      zip_safe=False,
      install_requires=[
        'setuptools >36',
        'six',
        'Zope >= 4',
        'Products.ZSQLMethods',
        ],
      extras_require={
        'exportimport': ['Products.GenericSetup > 2'],
        'docs': ['Sphinx;python_version >= "3"',
                 'Sphinx < 2;python_version < "3"',
                 'repoze.sphinx.autointerface'],
        },
      entry_points="""
      [zope2.initialize]
      %s = %s:initialize
      """ % (NAME, NAME),
      )

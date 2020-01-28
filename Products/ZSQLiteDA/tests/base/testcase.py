##############################################################################
#
# Copyright (c) 2000-2009 Jens Vagelpohl and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" A test case class for ZSQLiteDA tests
"""

import unittest

import transaction
from OFS.Folder import Folder
from Testing import ZopeTestCase

from Products.ZSQLiteDA.DA import manage_addZSQLiteConnection


class DATest(unittest.TestCase):

    def setUp(self):
        transaction.begin()
        self.app = self.root = ZopeTestCase.app()
        self.root._setObject('datest', Folder('datest'))
        self.folder = self.root.datest
        manage_addZSQLiteConnection(self.folder,id='da',title='DA',connection='da')
        da = self.folder.da

    def tearDown(self):
        transaction.abort()
        ZopeTestCase.close(self.app)

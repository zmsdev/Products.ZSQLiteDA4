##############################################################################
#
# Copyright (c) 2002 Zope Corporation and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
import os
from App.ImageFile import ImageFile
from . import DA
from . import standard
classes=('DA.Connection',)
database_type='SQLite'

misc_={'conn': ImageFile('images/DBAdapterFolder_icon.gif', globals()),
        'table': ImageFile('images/table.gif', globals()),
}

__module_aliases__=(
    ('Products.AqueductSQLite.DA', DA),
    )

def manage_addZSQLiteConnectionForm(self, REQUEST, *args, **kw):
    " "
    return DA.addConnectionForm(
        self, self, REQUEST,
        database_type=database_type,
        data_dir=standard.data_dir,
        data_sources=DA.data_sources)

def manage_addZSQLiteConnection(
    self, id, title, connection, REQUEST=None):
    " "
    return DA.manage_addZSQLiteConnection(
        self, id, title, connection, REQUEST)

def initialize(context):

    context.registerClass(
        DA.Connection,
        permission='Add Z SQLite Database Connections',
        constructors=(manage_addZSQLiteConnectionForm,
                      manage_addZSQLiteConnection),
        legacy=(manage_addZSQLiteConnectionForm,
                manage_addZSQLiteConnection),
    )


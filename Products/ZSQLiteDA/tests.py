import unittest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

def test_suite():
    return unittest.TestSuite([

        # Unit tests for your API
        doctestunit.DocFileSuite(
            'README.txt', package='Products.ZSQLiteDA',
            setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='Products.ZSQLiteDA.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        # Integration tests that use ZopeTestCase
        #ztc.ZopeDocFileSuite(
        #    'README.txt', package='Products.ZSQLiteDA',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #ztc.FunctionalDocFileSuite(
        #    'browser.txt', package='Products.ZSQLiteDA'),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

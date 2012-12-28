#!/usr/bin/python
# -*- coding: utf-8 -*-
try :
    import unittest2 as unittest
except (ImportError):
    import unittest

from unittest import TextTestRunner, TestCase
import tests

class AllTestCase(TestCase):
    def test_all(self):
        ttr = TextTestRunner(verbosity = 2)
        ttr.run(tests.get_all_test_suite())

if __name__== "__main__":
    atc = AllTestCase()
    atc.test_all()
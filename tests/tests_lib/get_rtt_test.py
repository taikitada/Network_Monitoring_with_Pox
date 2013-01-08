#!/usr/bin/python
# -*- coding: utf-8 -*-
try :
    import unittest2 as unittest
except (ImportError):
    import unittest
import sys,os
from os import path

CURRENT_DIR=path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIR + '/' + "../../")

from lib.get_rtt import get_rtt

class Get_rttTestCase(unittest.TestCase):

    def setUp(self):
        self.dest_host = "localhost"
        self.dest_host_fail = "localhost.fail"

    def tearDown(self):
        pass

    def test_get_rtt(self):
        with self.assertRaises(IndexError):
            get_rtt(self.dest_host_fail)

        self.result = get_rtt(self.dest_host)
        self.assertEqual(type(self.result), float)


if __name__ == "__main__":
    unittest.main()
#!/usr/bin/python
# -*- coding:utf-8 -*-
try :
    import unittest2 as unittest
except (ImportError):
    import unittest


import os, glob
from unittest import TestSuite, TestLoader, TextTestRunner

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_all test mods():
    '''import all tests from same directory '''
    test_mods = []
    pwd = os.getcwd()
    os.chdir(CURRENT_DIR)
    try:
        for file in glob.glob('*test.py'):
            test_mods.append(__import__(os.path.splitext(file.split('/')[-1])[0], globals(), locals(), []))
            return test_mods
    finally:
        os.chdir(pwd)

def get_all_test_pkgs():
    ''' import all packages defined as tests '''
    test_pkgs = []
    pwd = os.getcwd()
    os.chdir(CURRENT_DIR)
    try:
        for file in glob.glob('*/__init.py'):
            pkg = __import__(file.split('/')[0], globals(), locals(), [])
            if getattr(pkg, 'get_all_test_suite', None):
                test_pkgs.append(pkg)
        return test_pkgs
    finally:
        os.chdir(pwd)

def get_all_test_suite():
    ''' return all TestSuites included test '''
    all_tests = TestSuite()

    for tm in get_all_test_mods():
        suite = TestLoader().loadTestsFromModule(tm)
        all_tests.addTest(suite)

    for tp in get_all_test_pkgs():
        suite = TestLoader().loadTestsFromModule(tm)
        all_tests.addTest(suite)

    return all_tests

if __name__ == "__main__":
    ttr = TextTestRunner(verbosity = 2)
    ttr.run(get_all_test_suite())



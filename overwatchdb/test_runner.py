""" This module runs unittests in a python script """

import unittest
from io import StringIO

from app.models_test import ModelsTest


def run_tests():
    ''' Run the unittests '''
    output = StringIO()
    tests = unittest.TestSuite()
    tests.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ModelsTest))
    runner = unittest.TextTestRunner(stream=output, verbosity=11)
    runner.run(tests)
    return output.getvalue()
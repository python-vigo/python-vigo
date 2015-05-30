# -*- coding: utf-8 -*-

import unittest

import test_1
import test_2

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test_1)
suite.addTests(loader.loadTestsFromModule(test_2))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

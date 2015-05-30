# -*- coding: utf-8 -*-

import unittest

from ..test_1 import suma
from ..test_2 import division

class TestAll(unittest.TestCase):

    def test_suma(self):
        actual = suma(1,2)
        expected = 3
        self.assertEqual(expected, actual, 'suma(1,2) no es igual a 3')

    def test_division(self):
        actual = division(6, 2)
        expected = 3
        self.assertEqual(expected, actual, 'I should study maths')

    def test_that_fails(self):
        actual = division(6, 2)
        expected = -99
        self.assertEqual(expected, actual, 'I must study maths')

    def esto_no_es_un_test(self):
        actual = division(1.0, 2)
        expected = 0.5
        self.assertEqual(expected, actual, 'division(1.0, 2) no es igual a 0.5')

if __name__ == '__main__':
    unittest.main()

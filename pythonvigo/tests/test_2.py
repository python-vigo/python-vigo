# -*- coding: utf-8 -*-
# test_2.py

import unittest

def division(a, b):
    return a / b

class Example2Test(unittest.TestCase):
    def testMethod(self):
        actual = division(6, 2)
        expected = 3
        self.assertEqual(expected, actual, 'I should study maths')

    def test_that_fails(self):
        actual = division(6, 2)
        expected = -99
        self.assertEqual(expected, actual, 'I must study maths')

    def test_with_a_not_expected_error(self):
        actual = division(1, 0)
        expected = 0
        self.assertEqual(expected, actual, 'Are you serious')

    def esto_no_es_un_test(self):
        actual = division(1.0, 2)
        expected = 0.5
        self.assertEqual(expected, actual, 'division(1.0, 2) no es igual a 0.5')

if __name__ == '__main__':
    unittest.main()

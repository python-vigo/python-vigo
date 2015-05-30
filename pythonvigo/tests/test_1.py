# -*- coding: utf-8 -*-

import unittest

def suma(a, b):
    return a + b

class ExampleTest(unittest.TestCase):
    def testMethod(self):
        actual = suma(1,2)
        expected = 3
        self.assertEqual(expected, actual, 'suma(1,2) no es igual a 3')

if __name__ == '__main__':
    unittest.main()

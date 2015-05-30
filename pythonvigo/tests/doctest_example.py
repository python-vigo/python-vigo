# -*- coding: utf-8 -*-

import unittest

def division(a, b):
    '''
    Divides a with b

    >>> division(6, 2)
    3

    >>> division(10, 2)
    99
    '''
    return a / b

if __name__ == '__main__':
    import doctest
    doctest.testmod()

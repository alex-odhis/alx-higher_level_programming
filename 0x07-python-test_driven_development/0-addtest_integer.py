#!/usr/bin/python3

import unittest

addition = __import__('0-add_integer')

class TestAddInteger(unittest.TestCase):
    def test_add(self):
        #Test add positive numbers
        self.assertAlmostEqual(addition.add_integer(4, 3), 4 + 3)

    def test_add1(self):
        #Test add negative numbers
        self.assertAlmostEqual(addition.add_integer(-4, -3), -4 + -3)

if __name__ == '__main__':
    log_file = 'tests/0-add_integer.txt'
    with open( log_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)

#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_list(self):
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([1, -2000, 300]), 300)

    def test_values(self):
        self.assertRaises(TypeError, max_integer, ["one", 2, 4])
        self.assertRaises(TypeError, max_integer, -16)
        self.assertRaises(TypeError, max_integer, 1.4)
        self.assertRaises(TypeError, max_integer, -1.5)
        self.assertRaises(TypeError, max_integer, 5j)
        self.assertRaises(TypeError, max_integer, [6j, 2, 4])

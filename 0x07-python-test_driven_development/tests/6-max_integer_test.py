#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Tests - Functions max_integer
    """

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer(self):
        self.assertEqual(max_integer([7, 8, 9, 10]), 10)

    def test_max_integer(self):
        self.assertEqual(max_integer([9, 10, 7, 8]), 10)

    def test_max_integer(self):
        self.assertEqual(max_integer([-7, -8, -9, -10]), -7)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, 'hola mundo'])

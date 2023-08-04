#!/usr/bin/python3
"""Test_area module."""

import unittest
from area import area

class TestArea(unittest.TestCase):
    """Test area class."""

    def test_valid_parameters(self):
        b = area(2, 10)
        self.assertEqual(b, 20)

    def test_negative_height_width(self):
        with self.assertRaises(ValueError):
            area(-2, 20)

        with self.assertRaises(ValueError):
            area(20, -2)

        with self.assertRaises(ValueError):
            area(-2, -2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            area(0, 20)

    def test_floats(self):
        b = area(2.5, 4)
        self.assertEqual(b, 10)
        
        b = area(2.5, 3.5)
        self.assertEqual(b, 8.75)

    def test_non_integers(self):
        with self.assertRaises(TypeError):
            area('alex', 7)



        


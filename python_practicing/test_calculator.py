#!/usr/bin/python3

from calculator import add, sub, mul, div
import unittest
import numpy as np

class TestCalculator(unittest.TestCase):
    """Define TestCalculator Class."""

    """
    =================================================================
    test the add function:
    =================================================================
    """
    def test_valid_parameter(self):
        b = add(2, 10)
        self.assertEqual(b, 12)

        b = add(-2, 10)
        self.assertEqual(b, 8)

        b = add(-2, -10)
        self.assertEqual(b, -12)

        b = add(0, 0)
        self.assertEqual(b, 0)

    def test_string_parameter(self):
        with self.assertRaises(TypeError):
            add("alex", 2)

    def test_floats(self):
        b = add(2.5, 10)
        self.assertEqual(b, 12.5)

        b = add(2.5, 2.8)
        self.assertEqual(b, 5.3)

    def test_large_numbers(self):
        b = add(1000e99, 1000e99)
        self.assertEqual(b,2e102)

    def test_large_number(self):
        b = add(2e190, 2)
        self.assertAlmostEqual(b,2e190)

    def test_infinity(self):
        b = add(2e190, float('inf'))
        self.assertEqual(b, float('inf'))

    def test_infinity_both(self):
        b = add(float('inf'), float('inf'))
        self.assertEqual(b, float('inf'))

    def test_very_small_number(self):
        b = add(2e-1000, 2e120)
        self.assertAlmostEqual(b, 2e120)

    def test_greater(self):
        add(2, 10)
        self.assertGreater(10, 2)

        self.assertLess(2, 10)

    def test_None(self):
        with self.assertRaises(TypeError):
            add(5, None)

    def test_no_argument(self):
        with self.assertRaises(TypeError):
            add()

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            add(1)
    def test_more_than_two_args(self):
        with self.assertRaises(TypeError):
            add(2, 3, 4)

    def test_fraction(self):
        b = add(1/2, 1/4)
        self.assertEqual(b, 3/4)


    """
    =================================================================
    Test div function:
    =================================================================
    """

    def test_valid_parameters_div(self):
        b = div(10, 2)
        self.assertEqual(b, 5)

    def test_zero_quotient(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_to_get_decimal(self):
        b = div(5, 2)
        self.assertEqual(b, 2.5)

    def test_franction_div(self):
        b = div((1/2), (1/4))
        self.assertEqual(b, 2)

    def test_string_div(self):
        with self.assertRaises(TypeError):
            div('alex', 'jobs')

    def test_mixed_data(self):
        b = div(10, 2.5)
        self.assertEqual(b, 4)

    def test_division_with_fraction(self):
        b = div(10, 2/5)
        self.assertEqual(b, 25)

    def test_division_infinity(self):
        b = div( 100, float('inf'))
        self.assertEqual(b, 0)

    def test_divison_by_one(self):
        self.assertEqual(div(100, 1), 100)

    def test_division_large(self):
        b = div(8e100, 4e300)
        self.assertEqual(b, 2e-200)

    def test_division_small(self):
        b = div(100, 4e-300)
        self.assertTrue(np.allclose(b, 25e300))

    def test_divisin_by_negative(self):
        self.assertEqual(div(-100, 2), -50)
        self.assertEqual(div(-100, -2), 50)







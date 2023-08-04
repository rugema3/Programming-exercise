# test_string_calculator.py
import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(StringCalculator.add(""), 0)

    def test_single_number(self):
        self.assertEqual(StringCalculator.add("5"), 5)

    def test_two_numbers(self):
        self.assertEqual(StringCalculator.add("2,3"), 5)

    def test_multiple_numbers(self):
        self.assertEqual(StringCalculator.add("1,2,3,4,5"), 15)

    def test_numbers_with_newlines(self):
        self.assertEqual(StringCalculator.add("1\n2,3"), 6)

if __name__ == "__main__":
    unittest.main()

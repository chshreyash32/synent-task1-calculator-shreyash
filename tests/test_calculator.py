"""
Unit tests for the calculator module.
"""
import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.5, 3.7), 6.2)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(3, 3), 0)
        self.assertEqual(subtract(2.5, 1.2), 1.3)

    def test_multiplication(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(2.5, 4), 10.0)

    def test_division(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(10, 3), 10/3)
        self.assertEqual(divide(0, 5), 0)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(5, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))

if __name__ == '__main__':
    unittest.main()
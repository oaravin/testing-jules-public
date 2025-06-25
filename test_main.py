import unittest
from main import add # Assuming main.py is in the same directory or accessible via PYTHONPATH

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(10, 20), 30)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add(-3, -4), -7)
        self.assertEqual(add(-10, -20), -30)

    def test_add_positive_and_negative_numbers(self):
        """Test adding a positive and a negative number."""
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(10, -10), 0)

if __name__ == '__main__':
    unittest.main()

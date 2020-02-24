from django.test import TestCase

from app.calc import add
from app.calc import subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_number(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(10, 5), 5)
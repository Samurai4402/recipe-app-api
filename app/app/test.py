"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc modlule."""

    def test_add_numbers(self):
        """Test add numbers"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)


    def test_substract_numbers(self):
        """Test substract numbers"""
        res = calc.substract(5, 6)

        self.assertEqual(res, -1)

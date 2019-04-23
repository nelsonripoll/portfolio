import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Nelson Ripoll' work?"""
        formatted_name = get_formatted_name('nelson', 'ripoll')
        self.assertEqual(formatted_name, 'Nelson Ripoll')

    def test_first_last_middle_name(self):
        """Do names like 'Nelson Richard Ripoll' work?"""
        formatted_name = get_formatted_name('nelson', 'ripoll', 'richard')
        self.assertEqual(formatted_name, 'Nelson Richard Ripoll')

unittest.main()

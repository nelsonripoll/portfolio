import unittest
from employee import Employee 

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""
    def setUp(self):
        """Create base employee."""
        self.employee = Employee("Nelson", "Ripoll", 50000)

    def test_give_default_raise(self):
        """Give raise using default amount."""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 55000)

    def test_give_raise(self):
        """Give raise."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, 60000)

unittest.main()

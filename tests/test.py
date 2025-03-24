# Unit_Tests_Python/tests/test.py

import unittest
from code.calculations import Calculations

class TestCalculations(unittest.TestCase):
    
    def test_sum(self):
#       calculation = Calculations(8, 2)
        self.assertEqual(11, Calculations(8, 2).get_sum())
        
    def test_diff(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_difference(), 6, 'The difference is wrong.')
        
    def test_product(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_product(), 16, 'The product is wrong.')
        
    def test_quotient(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_quotient(), 4, 'The quotient is wrong.')
        
if __name__ == '__main__':
    unittest.main()
    
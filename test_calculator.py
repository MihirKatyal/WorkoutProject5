import unittest
from rpn_calculator import RPNCalculator

class TestRPNCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = RPNCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calculator.evaluate_expression("3 5 +"), 8)

    def test_subtraction(self):
        self.assertEqual(self.calculator.evaluate_expression("10 5 -"), -5)

    def test_multiplication(self):
        self.assertEqual(self.calculator.evaluate_expression("4 5 *"), 20)
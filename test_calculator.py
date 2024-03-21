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

    def test_division(self):    
        self.assertEqual(self.calculator.evaluate_expression("20 5 /"), 5)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.evaluate_expression("4 0 /")
    
    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate_expression("3 +")

    def test_invalid_operand(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate_expression('three 5 +')

if __name__ == '__main__':
    unittest.main()

import unittest
from actions.Actions_Operations import OperationsFunction
from actions.TestBase import SetUpClass


class MathOperations(SetUpClass):
    def test_numeric_numbers(self):
        math = OperationsFunction(self.driver)
        math.addition_operation()
        math.subtraction_operation()
        math.multiplication_operation()
        math.division_operation()


if __name__ == '__main__':
    unittest.main()

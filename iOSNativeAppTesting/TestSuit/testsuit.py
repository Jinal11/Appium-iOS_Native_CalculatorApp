import unittest

from test_cases.TestNumericNumbers import NumericNumbers
from test_cases.TestDecimalNumbers import DecimalNumbers
from test_cases.TestOperations import MathOperations

numeric_num_tests = unittest.TestLoader().loadTestsFromTestCase(NumericNumbers)
decimal_num_tests = unittest.TestLoader().loadTestsFromTestCase(DecimalNumbers)
operations_tests = unittest.TestLoader().loadTestsFromTestCase(MathOperations)


suite = unittest.TestSuite((numeric_num_tests, decimal_num_tests, operations_tests))

unittest.TextTestRunner(verbosity=2).run(suite)

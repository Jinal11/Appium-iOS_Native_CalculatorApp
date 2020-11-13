import unittest
from actions.Actions_Numeric import NumericActions
from actions.TestBase import SetUpClass


class NumericNumbers(SetUpClass):
    def test_numeric_numbers(self):
        numeric_no = NumericActions(self.driver)
        numeric_no.small_one_digit_number()
        numeric_no.small_two_digit_number()
        numeric_no.four_digit_number()
        numeric_no.eight_digit_number()


if __name__ == '__main__':
    unittest.main()

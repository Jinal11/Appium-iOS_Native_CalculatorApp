import unittest
from actions.Actions_Decimal import DecimalActions
from actions.TestBase import SetUpClass


class DecimalNumbers(SetUpClass):
    def test_decimal_numbers(self):
        decimal_no = DecimalActions(self.driver)
        decimal_no.small_decimal_number()
        decimal_no.medium_decimal_number()
        decimal_no.large_decimal_number()


if __name__ == '__main__':
    unittest.main()

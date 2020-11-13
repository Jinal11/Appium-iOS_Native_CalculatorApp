from elements.ElementsPage import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class DecimalActions(BasePage):

    def clear_all_numbers(self):
        clear_number = ElementsPage(self.driver).clear_numbers()
        clear_number.click()

    def small_decimal_number(self):
        self.clear_all_numbers()
        list_num = [0, '.', 1, 2]
        for a in list_num:
            number_button = ElementsPage(self.driver).button_number(a)
            number_button.click()
        verify_number = ElementsPage(self.driver).verification_number("0.12")
        assert verify_number == "0.12", "small decimal number not matched"

    def medium_decimal_number(self):
        self.clear_all_numbers()
        list_num = [8, 4, '.', 6, 2, 7]
        for a in list_num:
            number_button = ElementsPage(self.driver).button_number(a)
            number_button.click()
        verify_number = ElementsPage(self.driver).verification_number("84.627")
        assert verify_number == "84.627", "medium decimal number not matched"

    def large_decimal_number(self):
        self.clear_all_numbers()
        list_num = [8, 4, 5, 8, '.', 6, 2, 7, 3]
        for a in list_num:
            number_button = ElementsPage(self.driver).button_number(a)
            number_button.click()
        verify_number = ElementsPage(self.driver).verification_number("8,458.6273")
        assert verify_number == "8,458.6273", "large decimal number not matched"
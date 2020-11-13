from elements.ElementsPage import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class NumericActions(BasePage):

    def clear_all_numbers(self):
        clear_number = ElementsPage(self.driver).clear_numbers()
        clear_number.click()

    def small_one_digit_number(self):
        self.clear_all_numbers()
        number_button = ElementsPage(self.driver).button_number(8)
        number_button.click()
        verify_number = ElementsPage(self.driver).verification_number(8)
        assert verify_number == "8", "one digit decimal number not matched"

    def small_two_digit_number(self):
        self.clear_all_numbers()
        for i in range(0, 2):
            number_button = ElementsPage(self.driver).button_number(5)
            number_button.click()
        verify_number = ElementsPage(self.driver).verification_number(55)
        assert verify_number == "55", "two digit decimal number not matched"

    def four_digit_number(self):
        self.clear_all_numbers()
        for i in range(0, 4):
            number_button = ElementsPage(self.driver).button_number(7)
            number_button.click()
        verify_number = ElementsPage(self.driver).verification_number("7,777")
        assert verify_number == "7,777", "four digit decimal number not matched"

    def eight_digit_number(self):
        self.clear_all_numbers()
        list_num = [6, 2, 8, 1]
        for i in range(0, 2):
            for a in list_num:
                number_button = ElementsPage(self.driver).button_number(a)
                number_button.click()
        verify_number = ElementsPage(self.driver).verification_number("62,816,281")
        assert verify_number == "62,816,281", "eight digit decimal number not matched"

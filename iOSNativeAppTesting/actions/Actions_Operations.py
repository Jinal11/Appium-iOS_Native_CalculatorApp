from elements.ElementsPage import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class OperationsFunction(BasePage):

    def clear_all_numbers(self):
        clear_number = ElementsPage(self.driver).clear_numbers()
        clear_number.click()

    def addition_operation(self):
        self.clear_all_numbers()
        addition_array = [8, 'plus', 8, 'equal']
        for i in addition_array:
            number_button = ElementsPage(self.driver).button_number(i)
            number_button.click()
        verify_number = ElementsPage(self.driver).verification_number(16)
        assert verify_number == "16", "addition result not matched"

    def subtraction_operation(self):
        self.clear_all_numbers()
        addition_array = [1, 8, 'minus', 8, 'equal']
        for i in addition_array:
            number_button = ElementsPage(self.driver).button_number(i)
            number_button.click()
        verify_number = ElementsPage(self.driver).verification_number(10)
        assert verify_number == "10", "subtraction result not matched"

    def multiplication_operation(self):
        self.clear_all_numbers()
        addition_array = [1, 0, 'multiply', 1, 0, 'equal']
        for i in addition_array:
            number_button = ElementsPage(self.driver).button_number(i)
            number_button.click()
        verify_number = ElementsPage(self.driver).verification_number(100)
        assert verify_number == "100", "multiplication result not matched"

    def division_operation(self):
        self.clear_all_numbers()
        addition_array = [1, 0, 'divide', 1, 0, 'equal']
        for i in addition_array:
            number_button = ElementsPage(self.driver).button_number(i)
            number_button.click()
        verify_number = ElementsPage(self.driver).verification_number(1)
        assert verify_number == "1", "division result not matched"

class ElementsPage:
    def __init__(self, driver):
        self.driver = driver

    def button_number(self, xName):
        return self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='%s']" % xName)

    def clear_numbers(self):
        return self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='AC']")

    def verification_number(self, vNumber):
        return self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="%s"]' % vNumber)\
            .get_attribute("value")

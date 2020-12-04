import unittest
from appium import webdriver


# capabilities
class SetUpClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_cap = {
            "deviceName": "iPhone 11",
            "platformName": "iOS",
            "platformVersion": "14.2",
            "app": "/Users/Jinal/Library/Developer/Xcode/DerivedData/"
                   "CalculatorReplicaSwiftUI-agfoerdfhvadrbdfqzlbdtccyrbq/Build/"
                   "Products/Debug-iphonesimulator/Calculator.app",
            "noReset": 'true',
            "automationName": "XCUITest"
        }
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

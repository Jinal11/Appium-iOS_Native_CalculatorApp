'''
------------------------------------------------------------
This is RAW file before refactoring ----- Ignore this file.
------------------------------------------------------------
import time
from actions.TestBase import SetUpClass

# # capabilities
# desired_cap = {
#     "deviceName": "iPhone 11",
#   "platformName": "iOS",
#   "platformVersion": "14.0",
#   "app": "/Users/Jinal/Library/Developer/Xcode/DerivedData/CalculatorReplicaSwiftUI-agfoerdfhvadrbdfqzlbdtccyrbq/Build/Products/Debug-iphonesimulator/Calculator.app",
#   "noReset": 'true',
#   "automationName": "XCUITest"
# }
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
# driver.implicitly_wait(10)

# driver = SetUpClass().appSetUp() --AttributeError: 'NoneType' object has no attribute 'find_element_by_xpath'
driver = SetUpClass().appSetUp()
time.sleep(10)


# press 1 digit number
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="8"]') \
    .click()
typeNumber = driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="8"]').get_attribute("value")
assert typeNumber == "8", "Zero not available"

# press 2 digit number

driver.find_element_by_xpath("//XCUIElementTypeButton[@name='AC']").click()
for i in range(0, 2):
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="8"]').click()

typeNumber = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='88']").get_attribute("value")
print("the number is: ", typeNumber)
assert typeNumber == "88", "Number1 is invalid"

# press 3 digit number

driver.find_element_by_xpath("//XCUIElementTypeButton[@name='AC']").click()
for i in range(0, 3):
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="5"]').click()

typeNumber = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='555']").get_attribute("value")
print("the number is: ", typeNumber)
assert typeNumber == "555", "Number1 is invalid"

# press 8 digit number

driver.find_element_by_xpath("//XCUIElementTypeButton[@name='AC']").click()
for i in range(0, 2):
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="5"]').click()
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="4"]').click()
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="3"]').click()
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="2"]').click()

typeNumber = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='54,325,432']").get_attribute("value")
print("the number is: ", typeNumber)
assert typeNumber == "54,325,432", "Number1 is invalid"

# decimal number - small

driver.find_element_by_xpath("//XCUIElementTypeButton[@name='AC']").click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="0"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="."]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="1"]').click()

typeNumber = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='0.1']").get_attribute("value")
print("the number is: ", typeNumber)
assert typeNumber == "0.1", "Number is invalid"

# decimal number - medium

driver.find_element_by_xpath("//XCUIElementTypeButton[@name='AC']").click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="0"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="."]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="0"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="0"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="6"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="1"]').click()

typeNumber = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='0.0061']").get_attribute("value")
print("the number is: ", typeNumber)
assert typeNumber == "0.0061", "Number is invalid"

# decimal number - Large

driver.find_element_by_xpath("//XCUIElementTypeButton[@name='AC']").click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="1"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="0"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="1"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="4"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="."]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="6"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="8"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="4"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="7"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="7"]').click()

typeNumber = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='1,014.68477']").get_attribute("value")
print("the number is: ", typeNumber)
assert typeNumber == "1,014.68477", "Number is invalid"

# Addition - small number

driver.find_element_by_xpath("//XCUIElementTypeButton[@name='AC']").click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="2"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="plus"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="2"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="equal"]').click()

typeNumber = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='4']").get_attribute("value")
print("the number is: ", typeNumber)
assert typeNumber == "4", "Number is invalid"

# Minus - small number

driver.find_element_by_xpath("//XCUIElementTypeButton[@name='AC']").click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="2"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="minus"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="2"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="equal"]').click()

typeNumber = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='0']").get_attribute("value")
print("the number is: ", typeNumber)
assert typeNumber == "0", "Number is invalid"

# Multiplication - small number

driver.find_element_by_xpath("//XCUIElementTypeButton[@name='AC']").click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="2"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="multiply"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="2"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="equal"]').click()

typeNumber = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='4']").get_attribute("value")
print("the number is: ", typeNumber)
assert typeNumber == "4", "Number is invalid"

# Division - small number

driver.find_element_by_xpath("//XCUIElementTypeButton[@name='AC']").click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="2"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="divide"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="2"]').click()
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="equal"]').click()

typeNumber = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='1']").get_attribute("value")
print("the number is: ", typeNumber)
assert typeNumber == "1", "Number is invalid"
'''
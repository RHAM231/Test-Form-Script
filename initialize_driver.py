from tests import test_site_elements
from selenium_driver import TestDriver

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

def call_driver(data):
    testDriver = TestDriver()
    tabulation, testDriver = \
        test_site_elements.check_elements(data, testDriver)
    testDriver.tabulate_test_results(tabulation)
    testDriver.driver.quit()

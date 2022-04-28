##############################################################################
# PROJECT IMPORTS
##############################################################################

from tests.test_site_elements import check_elements
from selenium_driver import TestDriver, DriverHelper

##############################################################################
# BEGIN SCRIPT
##############################################################################


# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

def call_driver(data):
    # Initialize our driver.
    testDriver = TestDriver()
    # Run our tests for each page, returning the results.
    tabulation, testDriver = check_elements(data, testDriver)
    # Tabulate our results and print to terminal.
    DriverHelper().tabulate_results(tabulation)
    # Terminate our driver.
    testDriver.driver.quit()


##############################################################################
# END
##############################################################################

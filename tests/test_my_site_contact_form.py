##############################################################################
# IMPORTS
##############################################################################

import sys
sys.path.append('')
# Grab our test functionality from our main test script file.
from selenium_driver import TestDriver, DriverHelper
from data.my_site_form_data import MySiteFormData

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

##############################################################################
# BACKGROUND
##############################################################################


# Let's create a Python file for testing just my site's contact
# form. We'll import our functionality from our main test script file
# and run it from this file, giving it my site's test data for our
# contact form. This allows us to have different "buttons" to test
# different pieces of our three sites seperately. We don't necessarily
# want to test all three sites at the same frequency.

def submit_form(data, tdriver):
    tdriver.getURL(data)
    tdriver, results = tdriver.test_live_contact_form(data)
    return(results, tdriver)

if __name__ == '__main__':
    testDriver = TestDriver()
    form_data = MySiteFormData()
    testDriver.getURL(form_data)
    testDriver, results = testDriver.test_live_contact_form(form_data)
    DriverHelper().tabulate_results(results)
    testDriver.driver.quit()


##############################################################################
# END
##############################################################################

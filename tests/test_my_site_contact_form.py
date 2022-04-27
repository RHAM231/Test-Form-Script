##############################################################################
# IMPORTS
##############################################################################

import sys
sys.path.append('')
# Grab our test functionality from our main test script file.
from selenium_driver import TestDriver, mySiteData

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

def send_email(driver):
    driver.getURL(mySiteData)

if __name__ == '__main__':
    testDriver = TestDriver()
    testDriver.getURL(mySiteData)
    results = testDriver.test_live_contact_form(mySiteData)
    testDriver.tabulate_test_results(results)
    testDriver.driver.quit()


##############################################################################
# END
##############################################################################

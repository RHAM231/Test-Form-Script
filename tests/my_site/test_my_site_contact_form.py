##############################################################################
# PYTHON IMPORTS
##############################################################################

import sys
sys.path.append('')

##############################################################################
# PROJECT IMPORTS
##############################################################################

from selenium_driver import TestDriver, DriverHelper
from data.ms.my_site_form_data import MySiteFormData

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

##############################################################################
# BACKGROUND
##############################################################################


# Let's create a Python file for testing just my site's contact form.
# We'll import our functionality from our main test script file and run
# it from this file, giving it my site's HTML data. This allows us to
# have different "buttons" to test different pieces of our three sites
# seperately. We don't necessarily want to test all three sites at the
# same frequency.

# If we're called by another file (e.g test_my_site.py), just get the
# url from the given driver and run our test form script using the
# given data. Return the results and driver.
def submit_form(data, tdriver):
    tdriver.getURL(data)
    tdriver, results = tdriver.test_live_contact_form(data)
    return(results, tdriver)

# If this is the main running file, initialize our driver and data
# classes directly, run our tests, then tabulate the results and
# terminate our driver.
if __name__ == '__main__':
    # Initialize our driver and data.
    testDriver = TestDriver()
    form_data = MySiteFormData()
    # Test our contact form.
    testDriver.getURL(form_data)
    testDriver, results = testDriver.test_live_contact_form(form_data)
    # Tabulate the results to terminal.
    DriverHelper().tabulate_results(results)
    # Terminate our driver.
    testDriver.driver.quit()


##############################################################################
# END
##############################################################################

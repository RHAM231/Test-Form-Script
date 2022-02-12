##############################################################################
# IMPORTS
##############################################################################


# Grab our test data and our test functionality from our main test
# script file.
from test_form import HMSiteData, TestDriver


##############################################################################
# BACKGROUND
##############################################################################


# Let's create a Python file for testing just Hope Medical's contact
# form. We'll import our functionality from our main test script file
# and run it from this file, giving it Hope Medical's test data for our
# contact form. This allows us to have different "buttons" to test
# different pieces of our three sites seperately. We don't necessarily
# want to test all three sites at the same frequency.


##############################################################################
# DRIVING CODE
##############################################################################


# Intialize our Selenium driver object
testDriver = TestDriver()
# Pass our test data to driver
testDriver.getURL(HMSiteData)
# Call our test form functionality
testDriver.test_live_contact_form(HMSiteData)


##############################################################################
# END
##############################################################################

##############################################################################
# IMPORTS
##############################################################################


# Grab our test data and our test functionality from our main test
# script file.
from test_form import mySiteData, TestDriver


##############################################################################
# BACKGROUND
##############################################################################


# Let's create a Python file for testing just my site's contact
# form. We'll import our functionality from our main test script file
# and run it from this file, giving it my site's test data for our
# contact form. This allows us to have different "buttons" to test
# different pieces of our three sites seperately. We don't necessarily
# want to test all three sites at the same frequency.


testDriver = TestDriver()
testDriver.getURL(mySiteData)
testDriver.test_live_contact_form(mySiteData)


##############################################################################
# END
##############################################################################

##############################################################################
# IMPORTS
##############################################################################


# Grab our test data and our test functionality from our main test
# script file.

from test_form import mySiteData, TestDriver


testDriver = TestDriver()
testDriver.getURL(mySiteData)
testDriver.test_live_contact_form(mySiteData)

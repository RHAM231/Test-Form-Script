##############################################################################
# IMPORTS
##############################################################################

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

# Grab our test data and our test functionality from our main test
# script file.
from selenium_driver import TestDriver, HMSiteData

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

##############################################################################
# BACKGROUND
##############################################################################


# Let's create a Python file for testing just Hope Medical's contact
# form. We'll import our functionality from our main test script file
# and run it from this file, giving it Hope Medical's test data for our
# contact form. This allows us to have different "buttons" to test
# different pieces of our three sites seperately. We don't necessarily
# want to test all three sites at the same frequency.

# HMSiteData = {
#     # Hope Medical's contact form url
#     'url': 'https://www.hopemedicalwa.com/contact/',
#     # Hope Medical's contact form html id's and classes
#     'nameID': 'id_name',
#     'senderID': 'id_sender',
#     'subjectID': 'id_subject',
#     'messageID': 'id_message',
#     'checkboxID': 'id_cc_myself',
#     'submitCLASS': 'frm-btn',
#     # Hope Medical's contact form automated answers
#     'nameANSWER': 'Rex Mitchell',
#     'emailANSWER': 'nogardjmj@gmail.com',
#     'subjectANSWER': 'Automated Python Test',
#     'messageANSWER': (
#         'This is an automated test to verify the contact form is working'
#         ' properly.'
#         ),
# }

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

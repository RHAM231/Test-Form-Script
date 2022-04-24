##############################################################################
# IMPORTS
##############################################################################


# Grab our test functionality from our main test script file.
from test_form import TestDriver, mySiteData

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


# The url for the contact form and the form element id's and classes
# for my site
# mySiteData = {
#     # My contact form url
#     'url': 'https://rexhmitchell.com/contact/',
#     # My contact form html id's and classes
#     'nameID': 'id_name',
#     'senderID': 'id_sender',
#     'subjectID': 'id_subject',
#     'messageID': 'id_message',
#     'checkboxID': 'id_cc_myself',
#     'submitCLASS': 'frm-btn',
#     # My contact form automated answers
#     'nameANSWER': 'Python Test Script',
#     'emailANSWER': 'nogardjmj@gmail.com',
#     'subjectANSWER': 'Selenium Test',
#     'messageANSWER': (
#         'This is an automated test performed '
#         'by test_form.py using Selenium.'
#         ),
# }


testDriver = TestDriver()
testDriver.getURL(mySiteData)
# testDriver.test_live_contact_form(mySiteData)


##############################################################################
# END
##############################################################################

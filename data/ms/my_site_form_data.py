##############################################################################
# NO IMPORTS, BEGIN DATA CLASS
##############################################################################


# The url for the contact form and the form element id's and classes
# for my site
class MySiteFormData(object):
    def __init__(self):
        self.url = 'https://rexhmitchell.com/contact/'
        # My contact form html id's and classes
        self.nameID = 'id_name'
        self.senderID = 'id_sender'
        self.subjectID = 'id_subject'
        self.messageID = 'id_message'
        self.checkboxID = 'id_cc_myself'
        self.submitCLASS = 'frm-btn'
        # My contact form automated answers
        self.nameANSWER = 'Python Test Script'
        self.emailANSWER = 'nogardjmj@gmail.com'
        self.subjectANSWER = 'Selenium Test'
        self.messageANSWER = (
            'This is an automated test performed '
            'by test_form.py using Selenium.'
            )


##############################################################################
# END
##############################################################################

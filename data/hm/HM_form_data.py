# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

# The url for the contact form and the form element id's and classes
# for my site
class HMFormData(object):
    def __init__(self):
        self.url = 'https://www.hopemedicalwa.com/contact/'
        # Hope Medical's contact form html id's and classes
        self.nameID = 'id_name'
        self.senderID = 'id_sender'
        self.subjectID = 'id_subject'
        self.messageID = 'id_message'
        self.checkboxID = 'id_cc_myself'
        self.submitCLASS = 'frm-btn'
        # Hope Medical's contact form automated answers
        self.nameANSWER = 'Rex Mitchell'
        self.emailANSWER = 'nogardjmj@gmail.com'
        self.subjectANSWER = 'Automated Python Test'
        self.messageANSWER = (
            'This is an automated test to verify the '
            'contact form is working properly.'
            )

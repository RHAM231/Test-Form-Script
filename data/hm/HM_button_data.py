##############################################################################
# NO IMPORTS, BEGIN SCRIPTS
##############################################################################


# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

class HMSiteButtonData(object):
    def __init__(self):
        self.urls = {
                    'home': 'https://www.hopemedicalwa.com/',
                    'about': 'https://www.hopemedicalwa.com/about/',
                    'contact': 'https://www.hopemedicalwa.com/contact/',
                    'covid': 'https://www.hopemedicalwa.com/COVID',
                    'services': 'https://www.hopemedicalwa.com/services/',
                    'std': 'https://www.hopemedicalwa.com/STI_STD/',
                    'register': 'https://www.hopemedicalwa.com/register/',
                    'faqs': 'https://www.hopemedicalwa.com/FAQS/',
                    'support': 'https://www.hopemedicalwa.com/support_us/'
                    }
        self.ids = {
                    'home': [
                        '',
                        ],
                    '': [
                        '',
                        ],
                    'contact': [
                        'id_name', 'id_sender', 'id_subject', 'id_message', 
                        'id_cc_myself', 'submit-btn-id'
                        ],
                    'about': ['']
                    }


##############################################################################
# END
##############################################################################

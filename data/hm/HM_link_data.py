##############################################################################
# NO IMPORTS, BEGIN DATA CLASS
##############################################################################

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

# All the HTML classes and page urls for my site links.
class HMSiteLinkData(object):
    def __init__(self):
        self.urls = {
                'home': 'https://www.hopemedicalwa.com/',
                # 'about': 'https://www.hopemedicalwa.com/about/',
                # 'contact': 'https://www.hopemedicalwa.com/contact/',
                'covid': 'https://www.hopemedicalwa.com/COVID',
                'services': 'https://www.hopemedicalwa.com/services/',
                'std': 'https://www.hopemedicalwa.com/STI_STD/',
                'support': 'https://www.hopemedicalwa.com/support_us/'
                }
        self.classes = {
                        'home': (
                                "//*["
                                "@class='navbar-brand' or "
                                "@class='nav-link' or "
                                "@class='dropdown-item' or "
                                "@class='footer-link' or "
                                # "@class='ftr-info' or "
                                "@class='btn-square'"
                                "]"
                                ), 
                        # 'about': "//*[@class='class']",
                        # 'contact': "//*[""@class='class']",
                        'covid': "//*[@class='link-btn']",
                        'services': "//*[@class='link-btn']",
                        'std': "//*[@class='link-btn']",
                        'support': (
                                "//*["
                                "@class='link-btn' or "
                                "@class='btn-square'"
                                "]"
                                ),
                    }


##############################################################################
# END
##############################################################################

##############################################################################
# NO IMPORTS, BEGIN DATA CLASS
##############################################################################


# All the HTML classes and page urls for my site links.
class HMSiteLinkData(object):
    def __init__(self):
        self.urls = {
                'home': '', 
                '': '',
                '': (
                    ''
                    ),
                'about': ''
                }
        self.classes = {
                        'home': (
                                "//*["
                                "@class='class' or "
                                "@class='class'"
                                "]"
                                ), 
                        '': (
                                "//*["
                                "@class='class' or "
                                "@class='class'"
                                "]"
                                ),
                        '': "//*[""@class='class'""]",
                        'about': "//*[""@class='class'""]"
                    }


##############################################################################
# END
##############################################################################

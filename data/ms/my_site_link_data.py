##############################################################################
# PYTHON IMPORTS
##############################################################################

import sys
sys.path.append('')

##############################################################################
# PROJECT IMPORTS
##############################################################################

from initialize_driver import call_driver

##############################################################################
# BEGIN DATA CLASS
##############################################################################


# All the HTML classes and page urls for my site links.
class MySiteLinkData(object):
    def __init__(self):
        self.urls = {
                'home': 'https://rexhmitchell.com', 
                'portfolio': 'https://rexhmitchell.com/portfolio-project/',
                'checklist': (
                    'https://rexhmitchell.com/'
                    'portfolio-project/project_checklist/'
                    ),
                'about': 'https://rexhmitchell.com/about_me/'
                }
        self.classes = {
                        'home': (
                                "//*["
                                "@class='nav-link' or "
                                "@class='navbar-brand' or "
                                "@class='dropdown-item' or "
                                "@class='link-btn-light' or "
                                "@class='box' or "
                                "@class='here-link' or "
                                "@class='github-logo2'"
                                "]"
                                ), 
                        'portfolio': (
                                "//*["
                                "@class='link-btn' or "
                                "@class='here-link' or "
                                "@class='github-logo2'"
                                "]"
                                ),
                        'checklist': "//*[""@class='ref-link'""]",
                        'about': "//*[""@class='link-btn'""]"
                    }


##############################################################################
# END
##############################################################################

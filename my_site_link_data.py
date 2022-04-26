import test_site_elements
from selenium_driver import TestDriver

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

if __name__ == '__main__':
    testDriver = TestDriver()
    data = MySiteLinkData()
    tabulation, testDriver = \
        test_site_elements.check_elements(data, testDriver)
    testDriver.tabulate_test_results(tabulation)
    testDriver.driver.quit()

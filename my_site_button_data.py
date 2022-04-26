import test_site_elements
from selenium_driver import TestDriver


# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

class MySiteButtonData(object):
    def __init__(self):
        self.urls = {
                    'home': 'https://rexhmitchell.com/', 
                    'portfolio': \
                        'https://rexhmitchell.com/portfolio-project/',
                    'about': 'https://rexhmitchell.com/about_me/'
                    }
        self.ids = {
                    'home': [
                        'box-gh-id', 'box-ht5-id', 'box-git-id', 'box-aws-id',
                        'box-c3-id', 'box-ubt-id', 'box-js-id', 'box-dr-id',
                        'box-bst-id', 'box-pyt-id', 'box-dj-id',
                        'HM-btn-id', 'IT-btn-id', 'MS-btn-id'
                        ],
                    'portfolio': [
                        'github-btn-id', 'checklist-btn-id', 
                        'contact-btn-id'
                        ],
                    'about': ['contact-btn-id']
                    }


if __name__ == '__main__':
    testDriver = TestDriver()
    data = MySiteButtonData()
    tabulation, testDriver = \
        test_site_elements.check_elements(data, testDriver)
    testDriver.tabulate_test_results(tabulation)
    testDriver.driver.quit()

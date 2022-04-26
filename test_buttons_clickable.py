from selenium_driver import TestDriver
import time

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT
def set_links(page):
    ids = {
        'home': [
            'box-gh-id', 'box-ht5-id', 'box-git-id', 'box-aws-id', 
            'box-c3-id', 'box-ubt-id', 'box-js-id', 'box-dr-id',
            'box-bst-id', 'box-pyt-id', 'box-dj-id',
            'HM-btn-id', 'IT-btn-id', 'MS-btn-id'
            ],
        'portfolio': ['github-btn-id', 'checklist-btn-id', 'contact-btn-id'],
        'about': ['contact-btn-id']
    }
    return ids[page]

def check_buttons():
    testDriver = TestDriver()

    urls = {
        'home': 'https://rexhmitchell.com/', 
        'portfolio': 'https://rexhmitchell.com/portfolio-project/',
        'about': 'https://rexhmitchell.com/about_me/'
        }

    for page, url in urls.items():
        testDriver.getURL({'url': url})
        ids = set_links(page)

        print('\n', '########### ', page.upper(), 'Page ###########', '\n')
        testDriver.test_buttons_clickable(ids)

    testDriver.driver.quit()

check_buttons()
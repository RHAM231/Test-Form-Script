from selenium_driver import TestDriver


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

def check_buttons(driver=None):
    if __name__ == '__main__':
        testDriver = TestDriver()
    else:
        testDriver = driver
    urls = {
        'home': 'https://rexhmitchell.com/', 
        'portfolio': 'https://rexhmitchell.com/portfolio-project/',
        'about': 'https://rexhmitchell.com/about_me/'
        }
    tabulation = []
    for page, url in urls.items():
        testDriver.getURL({'url': url})
        ids = set_links(page)

        results = testDriver.test_buttons_clickable(page, ids)
        tabulation = tabulation + results

    if __name__ == '__main__':
        testDriver.tabulate_test_results(tabulation)
        testDriver.driver.quit()
    else:
        return (tabulation, testDriver)

if __name__ == '__main__':
    check_buttons()

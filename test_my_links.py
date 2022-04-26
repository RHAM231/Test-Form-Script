from selenium_driver import TestDriver


# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT


def set_links(page):
    classes = {
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
    return classes[page]


def check_links(driver=None):
    if __name__ == '__main__':
        testDriver = TestDriver()
    else:
        testDriver = driver

    urls = {
        'home': 'https://rexhmitchell.com/', 
        'portfolio': 'https://rexhmitchell.com/portfolio-project/',
        'checklist': \
            'https://rexhmitchell.com/portfolio-project/project_checklist/',
        'about': 'https://rexhmitchell.com/about_me/'
        }

    tabulation = []
    for page, url in urls.items():
        testDriver.getURL({'url': url})
        classes = set_links(page)
        results = testDriver.test_links(page, classes)
        tabulation = tabulation + results

    if __name__ == '__main__':
        testDriver.tabulate_test_results(tabulation)
        testDriver.driver.quit()
    else:
        return (tabulation, testDriver)

if __name__ == '__main__':
    check_links()

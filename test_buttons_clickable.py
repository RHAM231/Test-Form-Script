from test_form import TestDriver
import time

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT
def set_links(page):
    classes = {
        'home': (
                "//*["
                # "@class='nav-link' or "
                # "@class='navbar-brand' or "
                # "@class='dropdown-item' or "
                "@class='link-btn-light' or "
                "@class='box' or "
                "@class='github-logo2'"
                "]"
                ), 
        'portfolio': (
                "//*["
                "@class='link-btn' or "
                "@class='github-logo2'"
                "]"
                ),
        'about': (
                "//*["
                "@class='link-btn'"
                "]"
                )
    }
    return classes[page]

html_ids = [
            'box-gh-id', 'box-ht5-id', 'box-git-id', 'box-aws-id', 
            'box-c3-id', 'box-ubt-id', 'box-js-id', 'box-dr-id',
            'box-bst-id', 'box-pyt-id', 'box-dj-id',
            'HM-btn-id', 'IT-btn-id', 'MS-btn-id'
            ]

def check_buttons():
    testDriver = TestDriver()

    urls = {
        'home': 'https://rexhmitchell.com/', 
        # 'portfolio': 'https://rexhmitchell.com/portfolio-project/',
        # 'about': 'https://rexhmitchell.com/about_me/'
        }

    for page, url in urls.items():
        testDriver.getURL({'url': url})
        classes = set_links(page)

        print(
            '\n', 
            '################# ', 
            page.upper(), 
            'Page #################', 
            '\n'
            )
        testDriver.test_buttons_clickable(html_ids)

    testDriver.driver.quit()

check_buttons()
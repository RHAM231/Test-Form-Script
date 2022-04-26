from test_form import TestDriver


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


def check_links():
    testDriver = TestDriver()

    urls = {
        'home': 'https://rexhmitchell.com/', 
        'portfolio': 'https://rexhmitchell.com/portfolio-project/',
        'about': 'https://rexhmitchell.com/about_me/'
        }

    for page, url in urls.items():
        testDriver.getURL({'url': url})
        classes = set_links(page)
        testDriver.test_links(classes)

    testDriver.driver.quit()

check_links()

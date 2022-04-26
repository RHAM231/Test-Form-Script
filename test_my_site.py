import test_my_buttons_clickable, test_my_links
from selenium_driver import TestDriver

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

if __name__ == '__main__':
    testDriver = TestDriver()
    link_tabulation, testDriver = test_my_links.check_links(testDriver)
    btn_tabulation, testDriver = \
        test_my_buttons_clickable.check_buttons(testDriver)
    tabulation = link_tabulation + btn_tabulation

    testDriver.tabulate_test_results(tabulation)


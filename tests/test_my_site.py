from selenium_driver import TestDriver
from test_site_elements import check_elements
from data import my_site_button_data, my_site_link_data

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

if __name__ == '__main__':
    testDriver = TestDriver()
    link_data = my_site_link_data.MySiteLinkData()
    button_data = my_site_button_data.MySiteButtonData()

    link_tabulation, testDriver = check_elements(link_data, testDriver)
    btn_tabulation, testDriver = check_elements(button_data, testDriver)

    tabulation = link_tabulation + btn_tabulation
    testDriver.tabulate_test_results(tabulation)

    testDriver.driver.quit()


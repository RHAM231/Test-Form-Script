import sys
sys.path.append('')

from selenium_driver import TestDriver
from test_site_elements import check_elements
from data.my_site_button_data import MySiteButtonData
from data.my_site_link_data import MySiteLinkData
from data.my_site_form_data import MySiteFormData
from test_my_site_contact_form import submit_form

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

if __name__ == '__main__':
    testDriver = TestDriver()
    link_data = MySiteLinkData()
    button_data = MySiteButtonData()
    form_data = MySiteFormData()

    link_tabulation, testDriver = check_elements(link_data, testDriver)
    btn_tabulation, testDriver = check_elements(button_data, testDriver)
    form_tabulation, testDriver = submit_form(form_data, testDriver)

    tabulation = link_tabulation + btn_tabulation + form_tabulation
    testDriver.tabulate_test_results(tabulation)

    testDriver.driver.quit()


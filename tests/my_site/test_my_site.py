##############################################################################
# PTYHON IMPORTS
##############################################################################

import sys
sys.path.append('')

##############################################################################
# PROJECT IMPORTS
##############################################################################

from selenium_driver import TestDriver, DriverHelper
from data.ms.my_site_button_data import MySiteButtonData
from data.ms.my_site_link_data import MySiteLinkData
from data.ms.my_site_form_data import MySiteFormData
from tests.test_site_elements import check_elements
from test_my_site_contact_form import submit_form

##############################################################################
# BEGIN SCRIPT
##############################################################################


# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

# Let's create a script responsible for running all other test scripts
# for testing my site. This gives us a button to test everything at
# once.


# If we're running this file as our starting point ...
if __name__ == '__main__':
    # Initialize our custom selenium driver and site HTML element data.
    testDriver = TestDriver()
    link_data = MySiteLinkData()
    button_data = MySiteButtonData()
    form_data = MySiteFormData()

    # Call our run methods, passing our data and driver to them. We'll
    # get back a list of dictionary results and our driver to continue
    # passing to the next script.
    link_tabulation, testDriver = check_elements(link_data, testDriver)
    btn_tabulation, testDriver = check_elements(button_data, testDriver)
    form_tabulation, testDriver = submit_form(form_data, testDriver)

    # Now that we've collected all our results, let's add them to
    # together in the order we collected them. Then we'll call our
    # tabulation methods to print to terminal.
    tabulation = link_tabulation + btn_tabulation + form_tabulation
    DriverHelper().tabulate_results(tabulation)

    # Terminate the driver so it will stop running.
    testDriver.driver.quit()


##############################################################################
# END
##############################################################################

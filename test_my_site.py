import test_my_buttons_clickable, test_my_links
from selenium_driver import TestDriver


if __name__ == '__main__':
    link_tabulation = test_my_links.check_links()
    btn_tabulation = test_my_buttons_clickable.check_buttons()
    tabulation = link_tabulation + btn_tabulation

    tabulationDriver = TestDriver()
    tabulationDriver.tabulate_test_results(tabulation)


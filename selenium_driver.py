##############################################################################
# IMPORTS
##############################################################################

from typing import Dict
import requests
import inspect

from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver import ActionChains
# Import Service to resolve executable_path deprecation issue
from selenium.webdriver.chrome.service import Service
# Import "By" to resolve find_element() deprecation issues
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from update_driver import UpdateChromeDriver

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

##############################################################################
# BEGIN SCRIPT
##############################################################################


# Let's make a script to test submission of our live contact forms.
# We'll use the code from the article below as a starting point.

# https://towardsdatascience.com/automating-submission-forms-with-python-94459353b03e


##############################################################################
# CONTACT FORM TEST FUNCTIONS
##############################################################################

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\u001b[32m'
    WARNING = '\033[93m'
    FAIL = '\u001b[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Find HTML elements by id's as well as classes, return them as a list
def retrieveContactFormTextElements(driver, siteData):
    name_element = driver.find_element(By.ID, siteData.nameID)
    email_element = driver.find_element(By.ID, siteData.senderID)
    subject_element = driver.find_element(By.ID, siteData.subjectID)
    message_element = driver.find_element(By.ID, siteData.messageID)
    return [name_element, email_element, subject_element, message_element]


# Grab our questions and answers and zip them together. Fill out our
# form with the answers and return our updated driver
def answerContactFormTextQuestions(driver, siteData):
    name = siteData.nameANSWER
    email = siteData.emailANSWER
    subject = siteData.subjectANSWER
    message = siteData.messageANSWER
    answers = [name, email, subject, message]
    questions = retrieveContactFormTextElements(driver, siteData)
    for a, q in zip(answers, questions):
        q.send_keys(a)
    return driver


# Retrieve our checkbox element and check it
def answerCheckBox(driver, element_id):
    checkBox = driver.find_element(By.ID, element_id)
    action = ActionChains(driver)
    action.move_to_element_with_offset(checkBox, 1, 1)
    action.click()
    action.perform()
    return driver


# Grab our button and submit our form
def submit(driver, element_class):
    submit_btn = driver.find_element(By.CLASS_NAME, element_class)
    submit_btn.click()
    return (driver, submit_btn)

##############################################################################
# SELENIUM DRIVER CLASS AND SETUP METHODS
##############################################################################


# Let's create a driver class to better organize our different
# functions. Over time, we'll add functions to test more than just
# contact forms.
class TestDriver(object):
    # Instantiate our driver from Selenium
    def __init__(self):
        # Get the latest version.
        # print('\n', 'Retrieving the latest version of chromedriver ...', '\n')
        # UpdateChromeDriver.get_latest_version()
        # print('\n\n', 'Chromedriver successfully updated. Starting tests ...', '\n')

        # Add options setting to declutter log from chromedriver bug.
        # See https://stackoverflow.com/questions/64927909/failed-to-read-descriptor-from-node-connection-a-device-attached-to-the-system
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Set up driver
        s = Service("./chromedriver")
        self.driver = webdriver.Chrome(service=s, options=options)

    # Feed it an endpoint
    def getURL(self, siteData):
        # Get our url from our given data, initialize Selenium's
        # driver, and pass our url to driver
        if isinstance(siteData, Dict):
            url = siteData['url']
        elif isinstance(siteData, object):
            url = siteData.url
        self.driver.get(url)


##############################################################################
# TEST METHODS
##############################################################################


    # Run our test contact form functions above to test if a contact
    # form on a given, live site is working properly
    def test_live_contact_form(self, siteData):
        # Open the form in Chrome, fill it out, and submit it
        results = DriverHelper().set_page_header_rows('Contact Form')
        data = {}
        self.driver.maximize_window()
        try:
            self.driver = answerContactFormTextQuestions(self.driver, siteData)
            self.driver = answerCheckBox(self.driver, siteData.checkboxID)
            self.driver, btn = submit(self.driver, siteData.submitCLASS)
            data['msg'] = 'Email Sent Successfully'
        except WebDriverException:
            btn = None
            data['msg'] = 'FAIL: email not sent'

        DriverHelper().extract_attributes(results, data, btn)

        return (self, results)

    
    # Run our test registration form functions above to test if a
    # registration form on a given, live site is working properly
    def test_live_registration_form(self, siteData):
        # Open the form in Chrome, fill it out, and submit it
        self.driver.maximize_window()
        # self.driver = \
        #     answerRegistrationFormTextQuestions(self.driver, siteData)
        self.driver = answerCheckBox(self.driver, siteData.checkboxID)
        # self.driver = submit(self.driver, mySiteData['submitCLASS'])

        # Terminate our driver so our script will stop
        # self.driver.quit()

    # Check all the links which can be found using the provided HTML
    # classes.
    def test_links(self, page, classes):
        # Find the links given the classes.
        links = self.driver.find_elements_by_xpath(classes)

        # Set up our page header rows
        results = DriverHelper().set_page_header_rows(page)

        # Check the status codes of the links.
        for link in links:
            data = {}
            r = requests.head(link.get_attribute('href'))
            status = r.status_code

            if status == 200 or 301 or 302:
                data['msg'] = f'OK: {status}'
            elif status == 404:
                data['msg'] = f'FAIL: {status}'
            else:
                data['msg'] = f'FAIL: {status}'
            
            DriverHelper().extract_attributes(results, data, link)
        
        return results

    # Given a list of HTML element ids, check if the buttons are
    # clickable. Raise an exception if not. Tabulate the results to
    # terminal.
    def test_buttons_clickable(self, page, ids):
        # Initialize our results. This will be a list of dictionaries,
        # each dictionary corresponding to a button. Add the header row
        # for the page.

        # Set up our page header rows
        results = DriverHelper().set_page_header_rows(page)

        # For every id in the list ...
        for html_id in ids:
            # Initialize an empty dictionary
            data = {}
            # Try to retrieve the button and check if it can be
            # clicked. Raise a timeout exception after five seconds.
            try:
                # Try to get the button using WebDriverWait.
                element = WebDriverWait(self.driver, 5).until\
                    (EC.element_to_be_clickable((By.ID, html_id)))
                # Set our success message.
                data['msg'] = 'Success: element is clickable'

            # If we were unable to click the button after the delay,
            # raise an exception.
            except TimeoutException:
                # Get the button normally instead.
                element = self.driver.find_element(By.ID, html_id)
                # Set our fail message.
                data['msg'] = 'FAIL: element is not clickable'

            DriverHelper().extract_attributes(results, data, element)

        return results


##############################################################################
# HELPER METHODS
##############################################################################

class DriverHelper(object):
    def set_page_header_rows(self, page):
        columns = ('class', 'id', 'href', 'msg')
        pg_hdr = {col:f'{page.upper()} PAGE' for col in columns}
        sep_row = {col:'------------' for col in columns}
        results = [sep_row, pg_hdr, sep_row]
        return results

    def extract_attributes(self, results, data, element):
        # Extract pertinent label info to output to our table.
        for attr in ('class', 'href', 'id'):
            try:
                data[attr] = element.get_attribute(attr)
            # If we can't get it, set it to None.
            except WebDriverException:
                data[attr] = None
        # Add the button dictionary to our results list.
        results.append(data)

    def tabulate_results(self, results):
        # Create our data rows.
        rows = []
        for data in results:
            # Extract our data.
            html_class = data['class']
            html_id = data['id']
            if data['href'] == None:
                url = data['href']
            elif len(data['href']) > 50:
                url = data['href'][0:45] + ' ...'
            else:
                url = data['href']
            msg = data['msg']
            # Change the color of the result message to be green for
            # success and red for failure.
            if 'FAIL' in msg:
                result = f'{bcolors.FAIL}{msg}{bcolors.ENDC}'
            elif 'PAGE' in msg or '------------' == msg:
                result = msg
            else:
                result = f'{bcolors.OKGREEN}{msg}{bcolors.ENDC}'
            # Add our data to rows.
            rows.append([html_class, html_id, url, result])

        # Tabulate our rows with its header to terminal.
        print(tabulate(
            rows, 
            headers=['HTML Class', 'HTML Id', 'URL', 'Result']
            ), '\n'
            )


##############################################################################
# END
##############################################################################

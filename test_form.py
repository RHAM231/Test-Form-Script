##############################################################################
# IMPORTS
##############################################################################

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
# Import Service to resolve executable_path deprecation issue
from selenium.webdriver.chrome.service import Service
# Import "By" to resolve find_element() deprecation issues
from selenium.webdriver.common.by import By
from update_driver import UpdateChromeDriver

# from test_my_site_contact_form import mySiteData
# from test_hm_contact_form import HMSiteData
from selenium.common.exceptions import WebDriverException


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


# Find HTML elements by id's as well as classes, return them as a list
def retrieveContactFormTextElements(driver):
    name_element = driver.find_element(By.ID, mySiteData['nameID'])
    email_element = driver.find_element(By.ID, mySiteData['senderID'])
    subject_element = driver.find_element(By.ID, mySiteData['subjectID'])
    message_element = driver.find_element(By.ID, mySiteData['messageID'])
    return [name_element, email_element, subject_element, message_element]


# Grab our questions and answers and zip them together. Fill out our
# form with the answers and return our updated driver
def answerContactFormTextQuestions(driver, siteData):
    name = siteData['nameANSWER']
    email = siteData['emailANSWER']
    subject = siteData['subjectANSWER']
    message = siteData['messageANSWER']
    answers = [name, email, subject, message]
    questions = retrieveContactFormTextElements(driver)
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
    driver.find_element(By.CLASS_NAME, element_class).click()
    return driver

##############################################################################
# DRIVING CODE
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
        url = siteData['url']
        self.driver.get(url)

    # Check all the links which can be found using the provided HTML
    # classes.
    def test_links(self, classes):
        # Find the links given the classes.
        links = self.driver.find_elements_by_xpath(classes)

        # Check the status codes of the links.
        for link in links:
            r = requests.head(link.get_attribute('href'))
            print(link.get_attribute('href'), r.status_code)

    def test_buttons_clickable(self):
        elements = self.driver.find_elements(By.CLASS_NAME, 'link-btn-light')
        for element in elements:
            try:
                element.click()
                print('Success!')
            except WebDriverException:
                print("Element is not clickable")

    # Run our test contact form functions above to test if a contact
    # form on a given, live site is working properly
    def test_live_contact_form(self, siteData):
        # Open the form in Chrome, fill it out, and submit it
        self.driver.maximize_window()
        self.driver = answerContactFormTextQuestions(self.driver, siteData)
        self.driver = answerCheckBox(self.driver, mySiteData['checkboxID'])
        self.driver = submit(self.driver, mySiteData['submitCLASS'])

        # Terminate our driver so our script will stop
        self.driver.quit()
    
    # Run our test registration form functions above to test if a
    # registration form on a given, live site is working properly
    def test_live_registration_form(self, siteData):
        # Open the form in Chrome, fill it out, and submit it
        self.driver.maximize_window()
        # self.driver = \
        #     answerRegistrationFormTextQuestions(self.driver, siteData)
        self.driver = answerCheckBox(self.driver, mySiteData['checkboxID'])
        # self.driver = submit(self.driver, mySiteData['submitCLASS'])

        # Terminate our driver so our script will stop
        # self.driver.quit()


##############################################################################
# END
##############################################################################



HMSiteData = {
    # Hope Medical's contact form url
    'url': 'https://www.hopemedicalwa.com/contact/',
    # Hope Medical's contact form html id's and classes
    'nameID': 'id_name',
    'senderID': 'id_sender',
    'subjectID': 'id_subject',
    'messageID': 'id_message',
    'checkboxID': 'id_cc_myself',
    'submitCLASS': 'frm-btn',
    # Hope Medical's contact form automated answers
    'nameANSWER': 'Rex Mitchell',
    'emailANSWER': 'nogardjmj@gmail.com',
    'subjectANSWER': 'Automated Python Test',
    'messageANSWER': (
        'This is an automated test to verify the contact form is working'
        ' properly.'
        ),
}

# The url for the contact form and the form element id's and classes
# for my site
mySiteData = {
    # My contact form url
    'url': 'https://rexhmitchell.com/contact/',
    # My contact form html id's and classes
    'nameID': 'id_name',
    'senderID': 'id_sender',
    'subjectID': 'id_subject',
    'messageID': 'id_message',
    'checkboxID': 'id_cc_myself',
    'submitCLASS': 'frm-btn',
    # My contact form automated answers
    'nameANSWER': 'Python Test Script',
    'emailANSWER': 'nogardjmj@gmail.com',
    'subjectANSWER': 'Selenium Test',
    'messageANSWER': (
        'This is an automated test performed '
        'by test_form.py using Selenium.'
        ),
}
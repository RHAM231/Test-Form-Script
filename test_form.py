##############################################################################
# IMPORTS
##############################################################################

from selenium import webdriver
# Import Service to resolve executable_path deprecation issue
from selenium.webdriver.chrome.service import Service
# Import "By" to resolve find_element() deprecation issues
from selenium.webdriver.common.by import By


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
    driver.find_element(By.ID, element_id).click()
    return driver


# Grab our button and submit our form
def submit(driver, element_class):
    driver.find_element(By.CLASS_NAME, element_class).click()
    return driver


##############################################################################
# TEST DATA
##############################################################################


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
    'submitID': 'frm-btn',
    # My contact form automated answers
    'nameANSWER': 'Python Test Script',
    'emailANSWER': 'nogardjmj@gmail.com',
    'subjectANSWER': 'Selenium Test',
    'messageANSWER': (
        'This is an automated test performed '
        'by test_form.py using Selenium.'
        ),
    'cc_myselfANSWER': 'Uknwown'
}


HMSiteData = {
    # Hope Medical's contact form url
    'url': '',
    # Hope Medical's contact form html id's and classes
    'nameID': 'id_name',
    'senderID': 'id_sender',
    'subjectID': 'id_subject',
    'messageID': 'id_message',
    'checkboxID': 'id_cc_myself',
    'submitID': 'frm-btn',
    # Hope Medical's contact form automated answers
    'nameANSWER': 'Rex Mitchell',
    'emailANSWER': 'nogardjmj@gmail.com',
    'subjectANSWER': 'Automated Python Test',
    'messageANSWER': (
        'This is an automated test to verify the contact form is working'
        ' properly.'
        ),
    'cc_myselfANSWER': 'Uknwown'
}


##############################################################################
# DRIVING CODE
##############################################################################


# Run our test contact form functions above to test if a contact form
# on a given live site is working properly
def test_live_contact_form(siteData):
    # Get our url from our given data, initialize Selenium's driver and
    # pass our url to driver
    url = siteData['url']
    s = Service("./chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get(url)

    # Open the form in Chrome, fill it out, and submit it
    driver.maximize_window()
    driver = answerContactFormTextQuestions(driver, siteData)
    driver = answerCheckBox(driver, mySiteData['checkboxID'])
    driver = submit(driver, mySiteData['submitID'])

    # Terminate our driver so our script will stop
    driver.quit()


##############################################################################
# END
##############################################################################

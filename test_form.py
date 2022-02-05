##############################################################################
# IMPORTS
##############################################################################

from selenium import webdriver
# Import Service to resolve executable_path deprecation issue
from selenium.webdriver.chrome.service import Service
# Import "By" so we can get our submit button by xpath
from selenium.webdriver.common.by import By


##############################################################################
# BEGIN SCRIPT
##############################################################################


# Let's make a script to test submission of our live contact forms.
# We'll use the code from the article below as a starting point.

# https://towardsdatascience.com/automating-submission-forms-with-python-94459353b03e


##############################################################################
# FUNCTIONS
##############################################################################


# Find elements by id's as well as classes
def retrieveContactFormTextElements(driver):
    name_element = driver.find_element(By.ID, mySiteData['nameID'])
    email_element = driver.find_element(By.ID, mySiteData['senderID'])
    subject_element = driver.find_element(By.ID, mySiteData['subjectID'])
    message_element = driver.find_element(By.ID, mySiteData['messageID'])
    return [name_element, email_element, subject_element, message_element]


# Grab our questions and answers and zip together
def answerTextQuestions(driver, mscfa):
    name = mscfa['name']
    email = mscfa['email']
    subject = mscfa['subject']
    message = mscfa['message']
    answers = [name, email, subject, message]
    questions = retrieveContactFormTextElements(driver)
    for a, q in zip(answers, questions):
        q.send_keys(a)
    return driver


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
    'url': 'https://rexhmitchell.com/contact/',
    'nameID': 'id_name',
    'senderID': 'id_sender',
    'subjectID': 'id_subject',
    'messageID': 'id_message',
    'checkboxID': 'id_cc_myself',
    'submitID': 'frm-btn',
}


# My Site Contact Form Answers
mscfa = {
    'name': 'Python Test Script',
    'email': 'nogardjmj@gmail.com',
    'subject': 'Selenium Test',
    'message': (
        'This is an automated test performed '
        'by test_form.py using Selenium.'
        ),
    'cc_myself': 'Uknwown'
}


##############################################################################
# DRIVING CODE
##############################################################################


url = "https://rexhmitchell.com/contact/"
s = Service("./chromedriver")
driver = webdriver.Chrome(service=s)
driver.get(url)

driver.maximize_window()
driver = answerTextQuestions(driver, mscfa)
driver = answerCheckBox(driver, mySiteData['checkboxID'])
driver = submit(driver, mySiteData['submitID'])


##############################################################################
# END
##############################################################################

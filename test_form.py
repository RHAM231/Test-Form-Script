##############################################################################
# IMPORTS
##############################################################################

from selenium import webdriver
# Import Service to resolve executable_path deprecation issue
from selenium.webdriver.chrome.service import Service


##############################################################################
# BEGIN SCRIPT
##############################################################################


# Let's make a script to test submission of our contact form. We'll use
# the code from the article below as a starting point.

# https://towardsdatascience.com/automating-submission-forms-with-python-94459353b03e


##############################################################################
# FUNCTIONS
##############################################################################


# Use driver.find_element_by_id() as well as class
def retrieveTextElements(driver):
    name_element = driver.find_element_by_id('id_name')
    email_element = driver.find_element_by_id('id_sender')
    subject_element = driver.find_element_by_id('id_subject')
    message_element = driver.find_element_by_id('id_message')
    return [name_element, email_element, subject_element, message_element]


# 'id_cc_myself'
def retrieveCheckboxElement(driver, elementID):
    return driver.find_element_by_id(elementID)

# 'frm_btn'
def retrieveSubmitElement(driver, element_class):
    return driver.find_elements_by_class_name(element_class)


# Grab our questions and answers and zip together
def answerTextQuestions(driver, mscfa):
    name = mscfa['name']
    email = mscfa['email']
    subject = mscfa['subject']
    message = mscfa['message']
    answers = [name, email, subject, message]
    questions = retrieveTextElements(driver)
    for a, q in zip(answers, questions):
        q.send_keys(a)
    return driver


def answerCheckBox(driver, mscfa, element_id):
    cc_myself = mscfa['cc_myself']
    retrieveCheckboxElement(driver, element_id).click()
    return driver


# Grab our button and submit our form
def submit(driver, element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver


##############################################################################
# TEST DATA
##############################################################################


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


test = driver.find_element_by_xpath('frm_btn')

print(test)


# driver.maximize_window()
# driver = answerTextQuestions(driver, mscfa)
# driver = answerCheckBox(driver, mscfa, 'id_cc_myself')
# driver = submit(driver, 'frm_btn')


# def answerNameAge(driver, df, element_class, user_id):
#     name = df["names"][user_id]
#     age = df["ages"][user_id]
#     text_answers = [name, str(age)] # following the order in the form
#     text_questions = driver.find_elements_by_class_name(element_class)
#     for a,q in zip(text_answers,text_questions):
#         q.send_keys(a)
#     return driver


# def answerCheckBox(driver, df, element_class, user_id):
#     color_answer = df["colors"][user_id]
#     color_answer_index = color_index_dict[color_answer]
#     driver.find_elements_by_class_name(
#         element_class)[color_answer_index].click()
#     return driver


# def submit(driver, element_class):
#     driver.find_element_by_xpath(element_class).click()
#     return driver


# df = pd.read_csv("./submission_form_database.csv")
# text_question_element_class = "quantumWizTextinputPaperinputInput"
# checkbox_question_element_class = "appsMaterialWizToggleRadiogroupOffRadio"

# url = "https://forms.gle/WY7E9N8wkiMtziTD9"
# driver = webdriver.Chrome(executable_path="./chromedriver")
# for user_id in range(len(df)):
#     driver.get(url)
    
#     driver.maximize_window()
#     driver = answerNameAge(driver, df, text_question_element_class, user_id)
#     driver = answerCheckBox(
#         driver, 
#         df, 
#         checkbox_question_element_class, 
#         user_id
#         )
#     driver = submit(driver, submit_element_class)


##############################################################################
# END
##############################################################################

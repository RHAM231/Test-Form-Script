# Python Base Imports
import time
import json
from datetime import datetime
import pathlib
import glob
import sys
sys.path.append(".")

# Installed Packages
from selenium import webdriver
# Import Service to resolve executable_path deprecation issue
from selenium.webdriver.chrome.service import Service
# import pandas as pd
# import faker
# import numpy as np



# https://towardsdatascience.com/automating-submission-forms-with-python-94459353b03e


##############################################################################
# BEGIN SCRIPT
##############################################################################


s = Service("./chromedriver")
driver = webdriver.Chrome(service=s)
print(driver)

# driver.find_element_by_id()

# Not sure if I want to use a dictionary or direct variables here
my_site_input_tags = {
    'name_question_element_id': 'id_name',
    'email_question_element_id': 'id_sender',
    'subject_question_element_id': 'id_subject',
    'message_question_element_id': 'id_message',
    'submit_element_class': 'frm_btn',
}
name_question_element_id = 'id_name'
email_question_element_id = 'id_sender'
subject_question_element_id = 'id_subject'
message_question_element_id = 'id_message'
submit_element_class = 'frm_btn'


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

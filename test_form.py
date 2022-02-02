from selenium import webdriver
import pandas as pd
import time
import json
from datetime import datetime
import pathlib
import glob
import sys
sys.path.append(".")
import faker
import numpy as np
import pandas as pd


# https://towardsdatascience.com/automating-submission-forms-with-python-94459353b03e


f = faker.Faker()
colors = ["Blue","Pink","Black","White","Green"]


names = [f.name() for _ in range(100)]
ages =  [np.random.randint(18,65) for _ in range(100)]
color_choices = [np.random.choice(colors,1)[0] for _ in range(100)]


database = pd.DataFrame(dict(names=names, ages=ages, colors = color_choices))
database.to_csv("submission_form_database.csv", index=False)
database.head()

text_question_element_class = "quantumWizTextinputPaperinputInput"
checkbox_question_element_class = "appsMaterialWizToggleRadiogroupOffRadio"
submit_element_class = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'


def answerNameAge(driver, df, element_class, user_id):
    name = df["names"][user_id]
    age = df["ages"][user_id]
    text_answers = [name, str(age)] # following the order in the form
    text_questions = driver.find_elements_by_class_name(element_class)
    for a,q in zip(text_answers,text_questions):
        q.send_keys(a)
    
    return driver


color_index_dict = {"Blue": 0, "Pink": 1, "Black": 2, "White": 3, "Green": 4}

def answerCheckBox(driver, df, element_class, user_id):
    color_answer = df["colors"][user_id]
    color_answer_index = color_index_dict[color_answer]
    driver.find_elements_by_class_name(element_class)[color_answer_index].click()
    
    
    return driver


def submit(driver, element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver


df = pd.read_csv("./submission_form_database.csv")
text_question_element_class = "quantumWizTextinputPaperinputInput"
checkbox_question_element_class = "appsMaterialWizToggleRadiogroupOffRadio"

url = "https://forms.gle/WY7E9N8wkiMtziTD9"
driver = webdriver.Chrome(executable_path="./chromedriver")
for user_id in range(len(df)):
    driver.get(url)
    
    driver.maximize_window()
    driver = answerNameAge(driver, df, text_question_element_class, user_id)
    driver = answerCheckBox(driver, df, checkbox_question_element_class, user_id)
    driver = submit(driver, submit_element_class)


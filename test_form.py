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


f = faker.Faker()
colors = ["Blue","Pink","Black","White","Green"]


names = [f.name() for _ in range(100)]
ages =  [np.random.randint(18,65) for _ in range(100)]
color_choices = [np.random.choice(colors,1)[0] for _ in range(100)]


database = pd.DataFrame(dict(names=names, ages=ages, colors = color_choices))
database.to_csv("submission_form_database.csv", index=False)
database.head()
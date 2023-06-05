# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:54:34 2023

@author: Shahirah
"""

import glassdoor_scraper as gs
import pandas as pd

# path = "C:/Users/Shahirah/Documents/ds_salary_proj"

# df = gs.get_jobs('data scientist', 15, False, path, 15)

df = pd.read_csv('ds_salaries.csv')


df.company_location.nunique()
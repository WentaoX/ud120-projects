# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:10:42 2017

@author: WENTAO
"""

import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")

### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

maxnum = 0
minnum = 1000000
for x in data_dict.keys():
    if data_dict[x]["salary"] > maxnum and data_dict[x]["salary"] != 'NaN':
        maxnum = data_dict[x]["salary"]
    if data_dict[x]["salary"] < minnum:
        minnum = data_dict[x]["salary"]

print minnum
print maxnum

# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Professor Junbin Gao
Copyright: Professsor Junbin Gao, The University of Sydney Business School
           January 2017
"""

import numpy as np
import pandas as pd

# Loading the data from drinks.csv
drinks = pd.read_csv('drinks.csv')

# Check that the DataFrame was loaded correctly by viewing some basic 
# information by using
drinks.dtypes
drinks.info()

# View summary statistics of the DataFrame drinks by using the describe function
drinks.describe()

# We can use the data in any way we wiss. For example, extract a column from 
# DataFrame so that we have a series
A = drinks['beer_servings']

a_mean = drinks['beer_servings'].mean()


# Handling missing data
drinks_dirty = pd.read_csv('drinks.csv', na_filter=True)
drinks_dirty.describe(include='all') 

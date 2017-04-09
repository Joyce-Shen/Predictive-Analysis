# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Professor Junbin Gao
Copyright: Professsor Junbin Gao, The University of Sydney Business School
           January 2017
"""

import numpy as np

# loading data into the data variable which is a numpy array
data = np.loadtxt('ibmclose.txt')

# printing the data at the first row and first column
print(data[0,0])

# printing all the closing values 
print(data[:, 1])
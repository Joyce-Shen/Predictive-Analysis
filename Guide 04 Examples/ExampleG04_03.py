#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat 11 March 11:54:32 2017

@author: Professor Junbin Gao
Copyright: Professsor Junbin Gao, The University of Sydney Business School
           March 2017
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('ibmclose.txt')
times, x = data[:,0], data[:,1] 

#We only draw the first 50 prices
plt.scatter(times[:50], x[:50])
plt.ylabel('Closing Prices')
plt.xlabel('Times')
plt.title('IBM Stock Prices (Scattering)')

 
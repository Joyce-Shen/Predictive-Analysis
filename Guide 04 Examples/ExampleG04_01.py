#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat 11 March 11:23:43 2017

@author: Professor Junbin Gao
Copyright: Professsor Junbin Gao, The University of Sydney Business School
           March 2017
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('ibmclose.txt')
times, x = data[:,0], data[:,1] 

plt.plot(times, x)
plt.ylabel('Closing Prices')
plt.xlabel('Times')
plt.title('IBM Stock Prices')
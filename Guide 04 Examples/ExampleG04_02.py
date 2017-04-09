#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat 11 March 11:40:23 2017

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

# Please run the first section above, then the second section below
# More Features to be added
plt.grid()

# Then run the following section
N = times.size   # number of elements in times
# Move to a tighted x-axis
plt.xlim((1,N))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:04:22 2019

@author: oyewunmi
"""
import numpy as np
import matplotlib.pyplot as plt
from pylab import show, arange, sin, plot, pi

x = np.arange(0, 5, 0.1)
#print(x)
y = np.sin(x)
#print(y)
plt.plot(x,y)
show()

#using only the pylab module to implement the chart
#t = arange(0.0, 2.0, 0.01)
#s = sin(2 * pi * t)
#plot(t,s)
#
#show()


# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:49:00 2019

@author: oyewunmi oluwaseyi
"""

import numpy as np
import os
from matplotlib import pyplot as plt
import seaborn as sns
os.chdir('/home/oyewunmi/Documents/programming works/Artificial intelligence/Csv_files')
try:
    Bmi,Age=np.loadtxt('exercise.csv',delimiter=',',skiprows=1,usecols=(7,7),unpack=True)
       #Axis setup
   #fig=plt.figure()
   #axis=fig.add_subplot (111 ,aspect='equal' )
       # plotting the graph
#    plt.barh(Bmi,Age)
#    plt.show()


#    num_cols = ["Age", "Height", "Weight", "Duration",
#            "Heart_Rate", "Body_Temp", "Calories"]
#    sns.pairplot(frame[num_cols], size=2)
    print(len(list(Bmi)))
except FileNotFoundError:
	os.chdir('/home/oyewunmi/Documents/programming works/Artificial intelligence/Csv_files')

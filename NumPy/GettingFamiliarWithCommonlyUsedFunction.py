# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 00:51:15 2019

@author: oyewunmi oluwaseyi
The use of common function of numpy
reading and writing with files
"""
import numpy as np
i2=np.eye(2)# creates a diagonal matrix where the parameter is the no of rows
print(i2)
np.savetxt('useOfEyeFunction.txt',i2)#i2 was saved in a file stored in the system directory
m=np.loadtxt('diabetes.csv',delimiter=',',skiprows=1,usecols=10,unpack=True)
#print (v)
#The dates scheduler
import datetime
def datestr2num(s):
    'this function converts a date to a numerical integer'
    return datetime.datetime.strptime(s, "%d-%m-%Y").date().weekday()
datestr2num('29-01-2019')







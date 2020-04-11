#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:36:34 2019

@author: oyewunmi
"""

import numpy as np
from sklearn import linear_model
from sklearn import preprocessing
from sklearn import model_selection
import matplotlib.pyplot as plt
import seaborn as sns

# input data
data = '/home/oyewunmi/Documents/MicrosoftLabFiles/ML/diabetes.csv'

# loading the data
'''
Meaning of the various variables
Prg - pregnancy
pg - plasma glucose
dbp - Diastolic Blood Pressure
si - Serum Insulin
bmi - body max index
dp - Diabetes Pedigree
age - age
db - diabetic status
'''
# unpacking the data feature vector into different variables
userid = np.loadtxt(data, delimiter=',', skiprows=1, usecols=0, unpack=True)
Prg = np. loadtxt(data, delimiter=',', skiprows=1, usecols=1, unpack=True)
pg = np. loadtxt(data, delimiter=',', skiprows=1, usecols=2, unpack=True)
dbp = np. loadtxt(data, delimiter=',', skiprows=1, usecols=3, unpack=True)
si = np. loadtxt(data, delimiter=',', skiprows=1, usecols=4, unpack=True)
bmi = np. loadtxt(data, delimiter=',', skiprows=1, usecols=6, unpack=True)
dp = np. loadtxt(data, delimiter=',', skiprows=1, usecols=7, unpack=True)
age = np. loadtxt(data, delimiter=',', skiprows=1, usecols=8, unpack=True)
db = np. loadtxt(data, delimiter=',', skiprows=1, usecols=9, unpack=True)

# assigning each feature with thier respective user and putting in an array
input_feature_vector = []
user_id = []
Db = []
for i in range(15000):
	Userid=[userid[i]]
	Diabetes = [db[i]]
	feature = [Prg[i], pg[i], dbp[i], si[i], bmi[i], dp[i], age[i]]
#	print(feature)
	input_feature_vector.append(feature)
	user_id.append(Userid)
	Db.append(Diabetes)
diabetes_score = np.array(Db)
#print(input_feature_vector[0])
#print(user_id[0])
print(diabetes_score)




# plotting the data to see the feature vectors that are skewed and needs normalizing
#plt.plot(age, pg)
#plt.show()

# creating the classifier
classifier = linear_model.LogisticRegression(solver='liblinear', C=100)

# Splitting the data into a 70:30 ratio where 70 is used for training
#x_train = model_selection.train_test_split(input_feature_vector, )
#y_train
#x_test
#y_test
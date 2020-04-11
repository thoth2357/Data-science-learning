#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 11:45:46 2019

@author: oyewunmi
"""
import numpy as np
from sklearn import linear_model
from utilities import visualize_classifier
import matplotlib.pyplot as plt

# Define sample input data with two dimensional vectors and correspionding labels
x = np.array([[3.1, 7.2], [4, 6.7], [2.9, 8], [5.1, 4.5], [6, 5], [5.6, 5], [3.3, 0.4], [3.9 , 0.9], [2.8, 1], [0.5, 3.4], [1, 4], [0.6, 4.9]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3])
print(x)
# create the logisitic regression classifier
classifier = linear_model.LogisticRegression(solver='liblinear', C=100)

# Train the classifier
classifier.fit(x, y)

# Visualize the performance of the classfier
visualize_classifier(classifier, x, y)

prg, pg, dbp, si, bmi, dp, age, db
for i in userid, Prg, pg, dbp, si, bmi, dp, age, db:
	 print(i)
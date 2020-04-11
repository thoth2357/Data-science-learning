#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 21:07:14 2019

@author: oyewunmi
Creating a confusion matrix to see the performance of a classifier we shall be checking the naives Bayes classifier
"""

#importing all the necessary packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import Naives_Bayes_Classifier as NBC

#defining the sample labels 
true_labels = NBC.Y
predicted_labels = NBC.y_predict

#creating the confusion matrix
confusion_mtrx = confusion_matrix(true_labels, predicted_labels)

#Visualize the confusion matrix
plt.imshow(confusion_mtrx, interpolation='nearest', cmap=plt.cm.gray)
plt.title('Confusion matrix')
plt.colorbar()
ticks = np.arange(5)
plt.xticks(ticks, ticks)
plt.yticks(ticks, ticks)
plt.ylabel('True labels')
plt.xlabel('Predicted labels')
plt.show()

# Classification report
targets = ['Class-0', 'Class-1', 'Class-2', 'Class-3']
print('\n', classification_report(true_labels, predicted_labels,
target_names=targets))
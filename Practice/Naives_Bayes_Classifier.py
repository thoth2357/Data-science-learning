#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:31:26 2019

@author: oyewunmi
this is used to build classifier using bayes theorem
"""
#importing the necessary packages
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection
from utilities import visualize_classifier

# load data from input file
input_file = 'data_multivar_nb.txt'
data = np.loadtxt(input_file, delimiter=',')
X = data[:, :-1] #note X is the feature label that produce the outcome Y
Y = data[:, -1] #note Y is the true label/ outcome of the feature variables
#print(np.size(X))
#print(np.size(Y))

#Create the Naives Bayes Classifier
Classifier = GaussianNB()

#Training the Classifier
Classifier.fit(X, Y)

# Running the classifier on the data and predicting the outcome
y_predict = Classifier.predict(X)
#print(y_predict)
#print(X,y_predict)

#computing the accuracy of the data by comparing the predicted data with the true labels
accuracy = 100.0 * (Y == y_predict).sum() / X.shape[0]
print('The Accuracy of the NaivesBayes Classifier is {}%'.format(accuracy))

# Visualize the performance of the classifier
#visualize_classifier(Classifier, X, Y)

#Cross validation of the model 
"""Split the data into training and testing subsets. As specified by the test_size parameter in
the line below, we will allocate 80% for training and the remaining 20% for testing"""

# Split data into training and test data
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y,
test_size=0.2, random_state=3)
#print(np.size(X_train),np.size(X_test)
#print(np.size(y_train),np.size(y_test))

#create the new classifier
new_classifier = GaussianNB()

#Train the classifier with the splitted data (the 80% percent)
new_classifier.fit(X_train, y_train)

# Running the classifier on the splited data (the 20% percent) and predicting the outcome 
y_test_predict = new_classifier.predict(X_test)

#computing the accuracy of the data by comparing the predicted data with the true labels
Validation_accuracy = 100.0 * (y_test == y_test_predict).sum() / X_test.shape[0]
print('The Accuracy of theCross validation NaivesBayes Classifier is {}%'.format(Validation_accuracy))

# Visualize the performance of the classifier
#visualize_classifier(new_classifier, X_test, y_test)

#Calculating the other metrics
num_folds = 3
accuracy_values = model_selection.cross_val_score(Classifier,
X, Y, scoring='accuracy', cv=num_folds)
print("Accuracy: " + str(round(100*accuracy_values.mean(), 2)) + "%")

precision_values = model_selection.cross_val_score(Classifier,
X, Y, scoring='precision_weighted', cv=num_folds)
print("Precision: " + str(round(100*precision_values.mean(), 2)) + "%")

recall_values = model_selection.cross_val_score(Classifier,
X, Y, scoring='recall_weighted', cv=num_folds)
print("Recall: " + str(round(100*recall_values.mean(), 2)) + "%")

f1_values = model_selection.cross_val_score(Classifier,
X, Y, scoring='f1_weighted', cv=num_folds)
print("F1: " + str(round(100*f1_values.mean(), 2)) + "%")
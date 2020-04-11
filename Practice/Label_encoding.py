#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:27:45 2019

@author: oyewunmi
"""
from sklearn import preprocessing

input_labels = ['red', 'black', 'green', 'black', 'yellow', 'white']

# creating and training the label encoder
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

# print the mapping of the labels to their repective numbers
print('\nLabel mapping:')
for i, item in enumerate(encoder.classes_):
	print(item, '-->', i)

# Encoding a set of randomly ordered labels to see how it performs
test_labels = ['green', 'red', 'black']
encoded_test_labels = encoder.transform(test_labels)
print('\nLabels = ', test_labels)
print('Encoded values =', list(encoded_test_labels))

# Decoding a set of random values using the encoder
encoded_values = [3, 0, 4, 1]
decoded_values = encoder.inverse_transform(encoded_values)
print('\nEncoded values = ', encoded_values)
print('decoded_labels = ', list(decoded_values))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:24:16 2019

@author: oyewunmi
"""
import numpy as np
from sklearn import preprocessing

input_data = np.array([[5.1, -2.9, 3.3], [-1.2, 7.8, -6.1], [3.9, 0.4, 2.1], [7.3, -9.9, -4.5]])
print('The data in use is\n{}\n{}\n{}\n{}'.format(input_data[0], input_data[1], input_data[2], input_data[3]))
# binarizing the data using the threshold of 2.1
binarized_data = preprocessing.Binarizer(threshold=2.1).transform(input_data)
print('\nThe binarized data is ',binarized_data)

# mean removal
print('\n Mean and sd before mean removal')
print('Mean :{}\nstandard deviation {}'.format(input_data.mean(axis=0), input_data.std(axis=0)))
print('\n Mean and sd after mean removal')
data_scaled = preprocessing.scale(input_data)
print('Mean :{}\nstandard deviation {}'.format(data_scaled.mean(axis=0), data_scaled.std(axis=0)))

# Scaling data (min max scaling)
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print('\n The min max scaled data is :', data_scaled_minmax)

# Normalizing data
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
print('\nL1 normalized data:', data_normalized_l1)
print('\nL2 normalized data:', data_normalized_l2)


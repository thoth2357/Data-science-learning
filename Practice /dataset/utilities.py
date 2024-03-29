#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:01:31 2019

@author: oyewunmi
"""

import numpy as np
import matplotlib.pyplot as plt

def visualize_classifier(classifier, x, y, name):
	# define the minimum and maximum for x and y that will be used in the mesh grid
	min_x = x[:, 0].min() - 1.0
	max_x = x[:, 0].max() + 1.0
	min_y = x[:, 1].max() - 1.0
	max_y = x[:, 1].max() + 1.0

	mesh_step_size = 0.01
	x_vals, y_vals = np.meshgrid(np.arange(min_x, max_x, mesh_step_size), np.arange(min_y, max_y, mesh_step_size))

	#reshape the classifier on the mesh grid
	output = classifier.predict(np.c_[x_vals.ravel(), y_vals.ravel()])

	#Reshape the output array
	output = output.reshape(x_vals.shape)

	# Create a plot
	plt.figure()

	# Choose a color scheme for the plot
	plt.pcolormesh(x_vals, y_vals, output, cmap=plt.cm.gray)

	# Overlay the training points on the plot
	plt.scatter(x[:, 0], x[:, 1], c=y, s=75, edgecolors='black', linewidth=1, cmap=plt.cm.Paired)
	
	# setting the title of the graph
	plt.title(name)

	# Specify the boundaries of the plot
	plt.xlim(x_vals.min(), x_vals.max())
	plt.ylim(y_vals.min(), y_vals.max())

	# Specify the ticks on the X and Y axes
	plt.xticks((np.arange(int(x[:, 0].min() - 1), int(x[:, 0].max() + 1), 1.0)))
	plt.yticks((np.arange(int(x[:, 1].min() - 1), int(x[:, 1].max() + 1), 1.0)))
	plt.show()

    

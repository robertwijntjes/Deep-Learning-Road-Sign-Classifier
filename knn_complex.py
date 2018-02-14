#!/usr/bin/env python -W ignore::DeprecationWarning

# import the necessary packages
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import kneighbors_graph
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC

import numpy as np
import argparse
import cv2
import os,sys
from os import listdir
from os.path import isfile, join
from sklearn.externals import joblib
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import learning_curve
from sklearn.svm import SVC
import line_reader
import calculate_vector
# Important Imports

imagePaths_t1 = []
imagePaths_t2 = []
model_data = []
results = []

del sys.argv[0]
# Dynamic model creation
print(sys.argv)

# Features and Labels array
for a,i in enumerate(sys.argv):
    print(str(i))
    file_ = open(str(i),'r+')
    # Reads the files based on parameters given in command line

    imagePaths = line_reader.line_reader(file_)
    # Read Paths from directory files

    (features,labels) = calculate_vector.calculate_vectors(imagePaths)
    # Calculate Vectors from Paths

    (trnFeat, tstFeat, trnLabels, tstLabels) = train_test_split(features, labels, test_size=0.25, random_state=42)
    # Splits into Training and Testing Sets

    model = MLPClassifier (solver='lbfgs' , alpha=1e-5 , hidden_layer_sizes=(3, 10) , random_state = 1)
    # MLP Classifier for building Models

    model.fit(trnFeat,trnLabels)
    # Apply data to Classifier

    acc = model.score(tstFeat, tstLabels)
    # Score your Model on accuracy

    results.append('MLP HSV Accuracy '+ str(i) + ': ' + str(100 * acc) + '%')
    # Creates Results data

    joblib.dump(model, './models/'+ str(a) + '.pkl')
    # Creates Models for Classification


for i in results:
    print (i)
    # Shows Results
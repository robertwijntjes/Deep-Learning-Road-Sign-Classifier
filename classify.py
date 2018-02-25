from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui
import calculate_vector
import line_reader
import os,sys
import tree_mapper


imgData = []
features = []
paths = []
config = []
file_names = []

#del sys.argv[0]

f = easygui.fileopenbox()
I = cv2.imread(f)
# Read in Image

features = calculate_vector.calculate_single_path_v(I)
# Calculate and Transform Image


paths, file_names = line_reader.line_read_model(sys.argv[1])
# Reads in Models from

config = tree_mapper.tree_mapper()
# Reads the Config setup for the classifier stages


node = config['root']
# Gets first node of the config file




for a,i in enumerate(paths):
    pred = i.predict(features)

    for z in node:
        if pred[0] == z:
            print('Classifier Output: ' + pred[0] + '    :    Tree Strucure: ' + z + '   --> ' + 'Model: ' + file_names[a])
            node = config[z]

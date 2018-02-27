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
import model_puller


imgData = []
features = []
paths = []
config = []
file_names = []
combine = {}

#del sys.argv[0]
try:
    f = easygui.fileopenbox()
    I = cv2.imread(f)
except Exception,e:
    sys.exit("Wrong File Type Opened")
# Read in Image

features = calculate_vector.calculate_single_path_v(I)
# Calculate and Transform Image


paths, file_names = line_reader.line_read_model('./models/')

for i,a in enumerate(file_names):
    combine[file_names[i]] = paths[i]
# Laces up config to model directory


config = tree_mapper.tree_mapper()
# Reads the Config setup for the classifier stages

model_list = model_puller.model_puller()
print('Models: ' + str(model_list))


node = config['root']
# Gets first node of the config file


print('\n\n')
try:
    for a,i in enumerate(model_list):

        pred = combine[file_names[a]].predict(features)

        for z in node:
            if pred[0] == z:
                print('Classifier Output: ' + pred[0] + '    :    Tree Strucure: ' + z + '   --> ' + 'Model: ' + file_names[a])
                node = config[z]
except Exception,e:
    sys.exit("Warning: Model specification does not match Architecture specified.")

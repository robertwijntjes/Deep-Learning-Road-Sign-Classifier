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
import meta_dump
import time

clear = lambda: os.system('cls')
start_time = time.time()

imgData = []
features = []
paths = []
config = []
file_names = []
combine = {}
meta = []

#del sys.argv[0]
try:
    f = easygui.fileopenbox()
    I = cv2.imread(f)

except Exception as e:
    meta_dump.error_logger(["Wrong File Type Opened" , str(e)])
    sys.exit("Wrong File Type Opened" + str(e))
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
                meta.append('Classifier Output: ' + pred[0] + '    :    Tree Strucure: ' + z + '   --> ' + 'Model: ' + file_names[a])
                print('Classifier Output: ' + pred[0] + '    :    Tree Strucure: ' + z + '   --> ' + 'Model: ' + file_names[a])
                node = config[z]
                final_class = pred[0]
    print('\nPrediction: ' + final_class)
except Exception as e:
    meta_dump.error_logger(["Warning: Model specification does not match Architecture specified.\n" , str(e)])
    sys.exit("Warning: Model specification does not match Architecture specified.: " + str(e))


exectime = "Execution Time: " + "%.3f" % (time.time() - start_time) + " seconds"
print('\n'+ exectime)
meta_dump.classifier_data(meta,exectime)

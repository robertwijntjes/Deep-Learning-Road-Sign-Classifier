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


imgData = []
features = []
paths = []

#del sys.argv[0]

f = easygui.fileopenbox()
I = cv2.imread(f)
# Read in Image

features = calculate_vector.calculate_single_path_v(I)
# Calculate and Transform Image


paths = line_reader.line_read_model(sys.argv[1])
# Reads in Models from

for a,i in enumerate(paths):
    pred = i.predict(features)
    
    print('Round ' + str(a) + ':')
    print(pred)

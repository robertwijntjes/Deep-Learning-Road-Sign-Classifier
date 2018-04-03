import numpy as np
import argparse
import cv2
import os,sys
from os import listdir
from os.path import isfile, join
import meta_dump
from matplotlib import pyplot as plt



def calculate_vectors( array_file ):

    extPicture = []
    ImgLabel = []
    try:
        print('Begin Loading Images')
        for i , imagePath in enumerate( array_file ):
            #print('-- Loading Images --')
            path = cv2.imread(imagePath)
            label = imagePath.split(os.path.sep)[-1].split('/')[1]
            # Read in Image Paths i

            #path = cv2.cvtColor(path, cv2.COLOR_BGR2HSV)

            conv = ( 8 , 8 , 8 )
            hist = cv2.calcHist([path], [0, 1, 2], None, conv,[0, 180, 0, 256, 0, 256])
            hist = cv2.normalize(hist,hist)

            extPicture.append(hist.flatten())
            ImgLabel.append(label)

            # Applying i image data to sections
        print('End Loading Images\n')

        # Setting Image Data for Classification
        features = np.array(extPicture)
        labels = np.array(ImgLabel)

    except Exception,e:
        meta_dump.error_logger(["Invalid File Type Present in the Directory",str(e)])
        sys.exit("Invalid File Type Present in the Directory")
    return(features,labels)
    # Reads in all the images using the image paths and transforms




def calculate_single_path_v( path ):
    imgData = []
    features = []
    try:
        conv = (8,8,8)
        hist = cv2.calcHist([path], [0, 1, 2], None, conv,[0, 180, 0, 256, 0, 256])
        hist = cv2.normalize(hist,hist)
        imgData.append(hist.flatten())
        features = np.array(imgData)


        #color = ('b','g','r')
        #for i,col in enumerate(color):
        #    hist = cv2.calcHist(path,[i],None,conv,[0, 180, 0, 256, 0, 256])
        #    plt.plot(hist,color = col)
        #    plt.xlim([0,255])
        #plt.show()

    except Exception,e:
        meta_dump.error_logger(["Invalid File Type Present in the Directory",str(e)])
        sys.exit("Invalid File Type Present in the Directory" + str(e))
    return( features )
    # Reads in a single image for the classification file

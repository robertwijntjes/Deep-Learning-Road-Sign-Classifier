import numpy as np
import argparse
import cv2
import os,sys
from os import listdir
from os.path import isfile, join

def color_transform( vectors ):
        vectors = cv2.fastNlMeansDenoisingColored(vectors,None,10,10,7,21)
        hsv = cv2.cvtColor(vectors,cv2.COLOR_BGR2HSV)
        return ( hsv )


#hsv = color_transform.color_transform(path)

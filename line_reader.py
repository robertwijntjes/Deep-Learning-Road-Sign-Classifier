import os,sys
from os import listdir
from os.path import isfile, join
from sklearn.externals import joblib



def line_reader( files ):
    paths = []
    imagePaths = []

    for i,line in enumerate(files):
        paths.append(line.strip('\n'))


    for i in paths:
            imagePaths += [ i + files for files in listdir(i) if isfile(join(i, files))]

    return ( imagePaths )


def line_read_model( files ):
    imagePaths = []
    models = []

    imagePaths = [files + i for i in listdir(files) if isfile(join(files, i))]
    models += [joblib.load(models) for models in imagePaths]

    return ( models )


def string_parser( string_item ):

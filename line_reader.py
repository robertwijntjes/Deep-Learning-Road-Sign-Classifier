import os,sys
from os import listdir
from os.path import isfile, join
from sklearn.externals import joblib
import re
import pathlib



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
    line_ = []
    x = []
    raw_line_ = os.path.splitext(string_item)[0]
    regex = re.compile('[^a-zA-Z]')

    for i in raw_line_:
        line_ += regex.sub('', str(i))

    x = ''.join(line_)

    return ( x )




def file_parser( string_item , pos ):
    line_ = []
    x = []
    raw_line_ = os.path.splitext(string_item)[0]
    regex = re.compile('[^a-zA-Z]')

    if not os.path.exists('./models'):
        os.makedirs('models')

    for i in raw_line_:
        line_ += regex.sub('', str(i))

    x = ''.join(line_)
    z = './models/' + str(pos + 1)+ '_' + x + '.pkl'

    return ( z )

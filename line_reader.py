import os,sys
from os import listdir
from os.path import isfile, join
from sklearn.externals import joblib
import re
import pathlib



def line_reader( files ):
    paths = []
    imagePaths = []
    try:
        for i,line in enumerate(files):
            paths.append(line.strip('\n'))


        for i in paths:
                imagePaths += [ i + files for files in listdir(i) if isfile(join(i, files))]
    except Exception,e:
        sys.exit(e)

    return ( imagePaths )
    # Reads in all files in a directory


def line_read_model( files ):
    imagePaths = []
    models = []
    try:
        imagePaths = [files + i for i in listdir(files) if isfile(join(files, i))]
        models += [joblib.load(models) for models in imagePaths]
    except Exception,e:
        sys.exit("Wrong File type Present in ./Model/ folder!")

    return ( models , imagePaths )
    # Reads in all Models from a directory



def file_parser( string_item , pos ):
    line_ = []
    x = []
    subfolder = ['Builder Data','Classifier Data']
    raw_line_ = os.path.splitext(string_item)[0]
    regex = re.compile('[^a-zA-Z]')

    if not os.path.exists('./models'):
        os.makedirs('models')

    if not os.path.exists('config.txt'):
        config = open("config.txt","w")
        config.write("@\n\n@\n\n/\n\n/\n\n\n\nBuild your tree architecure inbetween the two AT symbols using the format -->\n\nroot : A B\nA: C D\nB: E F\n\n--------------------------------------------\n\nList the Location of your Models and the correct order to be read in between the two SLASH symbols\nusing the format --->\n\n./folder/model_1\n./folder/model_2")

    if not os.path.exists('./metadata'):
        for i in subfolder:
            os.makedirs(os.path.join('metadata',i))



    for i in raw_line_:
        line_ += regex.sub('', str(i))

    x = ''.join(line_)
    z = './models/' + str(pos + 1)+ '_' + x + '.pkl'

    return ( z )

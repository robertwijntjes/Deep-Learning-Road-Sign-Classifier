import time
import os,sys

def builder_data( file_ , time_):
    try:
        metadata = open('./metadata/Builder Data/' + time.strftime("%Y%m%d-%H%M%S") + '.txt',"w")
    except Exception,e:
        sys.exit("Cannot Post Metadata file to ./Metadata/Builder Data")
    for i in file_:
        metadata.write(i  + '\n')

    metadata.write(time_)

def classifier_data( file_ , time_ ):
    try:
        metadata = open('./metadata/Classifier Data/' + time.strftime("%Y%m%d-%H%M%S") + '.txt',"w")
    except Exception,e:
        sys.exit("Cannot Post Metadata file to ./Metadata/Classifier Data")
    for i in file_:
        metadata.write(i  + '\n')

def error_logger( error_ ):
    try:
        metadata = open('./metadata/Error Logs/' + time.strftime("%Y%m%d-%H%M%S") + '.txt',"w")
    except Exception,e:
        sys.exit("Cannot Post Error Log to ./Metadata/Error Logs: " + str(e))
    for i in error_:
        metadata.write(i  + '\n')

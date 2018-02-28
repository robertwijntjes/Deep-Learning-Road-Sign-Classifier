import time

def builder_data( file_ , time_):
    try:
        metadata = open('./metadata/Builder Data/' + time.strftime("%Y%m%d-%H%M%S") + '.txt',"w")
    except Exception,e:
        sys.exit("Cannot Post Metadata file to ./Metadata/Builder Data")
    for i in file_:
        metadata.write(i  + '\n')

    metadata.write(time_)
def classifier_data( file_ ):
    try:
        metadata = open('./metadata/Classifier Data/' + time.strftime("%Y%m%d-%H%M%S") + '.txt',"w")
    except Exception,e:
        sys.exit("Cannot Post Metadata file to ./Metadata/Classifier Data")

    metadata.write(file_)

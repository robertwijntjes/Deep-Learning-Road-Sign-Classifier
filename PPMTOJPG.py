import os,sys
from os import listdir
from os.path import isfile, join
from sklearn.externals import joblib
import re
import pathlib
from PIL import Image

def img_change():
	paths = []
	imagePaths = []
	print (sys.argv[1])
	try:
		imagePaths += [ str(sys.argv[1]) +  files for files in listdir(sys.argv[1]) if isfile(join(sys.argv[1], files))]
		os.makedirs('S')
		for i,j in enumerate(imagePaths):
			im = Image.open(j)
			
			im.save('./S/'+ str(i) + '-x.jpg')
			
			
			
	except Exception,e:
		sys.exit(e)

	return ( imagePaths )
	
img_change()
from Tkinter import *
import easygui
import cv2
import numpy as np

f = easygui.fileopenbox()
img = cv2.imread(f)
rtn = img.copy()
#img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

blank = np.zeros(np.shape(img),np.uint8)
blank[:,:] = (0,0,0)
tblank = cv2.cvtColor(blank, cv2.COLOR_BGR2GRAY)

colors = {
    "red" : [np.array([0, 0, 70]), np.array([[200, 56, 255]])]
    }

keys = colors.keys()
for color in keys:
    lower = colors.get(color)[0]
    upper = colors.get(color)[1]
    
    mask = cv2.inRange(img, lower, upper)
    maskImg = cv2.bitwise_and(img, img, mask = mask)

    gray = cv2.cvtColor(maskImg, cv2.COLOR_BGR2GRAY)
    k = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]], dtype=float)
    F = cv2.filter2D(gray, ddepth=-1, kernel=k)

    
    edge = cv2.Canny(F, 100, 200)
    E = cv2.dilate(edge, None, iterations = 1)

    (_, contours, _) = cv2.findContours(E.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
    contours = sorted(contours, key=cv2.contourArea,reverse=True)

    
    #cv2.drawContours(img, contours, 0, (0,0,0), 3)

    cv2.drawContours(rtn, contours, 0, (0,0,0), 3)
    ret,thresh1 = cv2.threshold(rtn,127,255,cv2.THRESH_BINARY)

    


    
#cv2.imshow("Original", img)
cv2.imshow("Colour Segmentation", rtn)
key = cv2.waitKey(0)

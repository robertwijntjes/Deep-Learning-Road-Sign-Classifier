import cv2
from pprint import pprint

img = cv2.imread('x.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
pprint(gray_img)

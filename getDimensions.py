
import numpy as np
import cv2
import sys

#this is the path to the folder where the image is stored
imgPath="c:\\wamp\\www\\web-landmark-detection\\"

imgName= sys.argv[1]
#print imgName
imgName=imgPath+imgName
#print imgName
img=cv2.imread(imgName,0)
#print img
height, width = img.shape

print 'h: ',height,"  w: ",width

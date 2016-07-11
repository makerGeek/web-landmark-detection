
import numpy as np
import cv2
import sys
import json
import base64
import os, cgi

# print
def getDimensions( image ):
    img=cv2.imread(image,0)
    # print img
    height, width = img.shape
    dimensions ={'height': height, 'width': width}
    dumped=json.dumps(dimensions)
    print
    print dumped

query = os.environ.get('QUERY_STRING')
arguments = cgi.parse_qs(query) if query else {}
if(arguments):
    imgName=arguments["image"]
    imgName= str(imgName[0])
    print imgName
    #this is the path to the folder where the image is stored
    image="c:\\wamp\\www\\web-landmark-detection\\cgi-bin\\"+imgName
    # print imgPath
    getDimensions(image)

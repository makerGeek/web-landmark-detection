
import numpy as np
import cv2
import sys
import json

import os, cgi
# print
query = os.environ.get('QUERY_STRING')
arguments = cgi.parse_qs(query) if query else {}
if(arguments):
    imgName=arguments["image"]
    imgName= str(imgName[0])

    #this is the path to the folder where the image is stored
    imgPath="c:\\wamp\\www\\web-landmark-detection\\cgi-bin\\"+imgName
    # print imgPath

    img=cv2.imread(imgPath,0)
    # print img

    height, width = img.shape
    dimensions ={'height': height, 'width': width}
    dumped=json.dumps(dimensions)
    print
    print dumped

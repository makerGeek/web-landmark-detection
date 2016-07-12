"""This demonstrates a minimal http upload cgi.
This allows a user to upload up to three files at once.
It is trivial to change the number of files uploaded.

This script has security risks. A user could attempt to fill
a disk partition with endless uploads.
If you have a system open to the public you would obviously want
to limit the size and number of files written to the disk.
"""
import cgi
import cgitb; cgitb.enable()
import os, sys
import get_landmarks
import numpy as np
import cv2
import sys
import json
import base64
import os, cgi
try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

UPLOAD_DIR = "tmp"
IMAGE ='none'
IMAGE_AVAILABLE = False

HTML_TEMPLATE = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><head><title>File Upload</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head><body><h1>Upload face</h1>
<form action="%(SCRIPT_NAME)s" method="POST" enctype="multipart/form-data">
File name: <input name="file_1" type="file"><br>
<input name="submit" type="submit">
</form>
</body>
</html>"""



def print_html_form ():
    """This prints out the html form. Note that the action is set to
      the name of the script which makes this is a self-posting form.
      In other words, this cgi both displays a form and processes it.
    """
    print "content-type: text/html\n"
    print HTML_TEMPLATE % {'SCRIPT_NAME':os.environ['SCRIPT_NAME']}

def save_uploaded_file (form_field, upload_dir):
    """This saves a file uploaded by an HTML form.
       The form_field is the name of the file input field from the form.
       For example, the following form_field would be "file_1":
           <input name="file_1" type="file">
       The upload_dir is the directory where the file will be written.
       If no file was uploaded or if the field does not exist then
       this does nothing.
    """
    form = cgi.FieldStorage()
    if not form.has_key(form_field): return
    fileitem = form[form_field]
    if not fileitem.file: return
    try:
        fout = file (os.path.join(upload_dir, fileitem.filename), 'wb')
        global IMAGE
        IMAGE = str(upload_dir)+"\\"+str(fileitem.filename)

        while 1:
            chunk = fileitem.file.read(100000)
            if not chunk: break
            fout.write (chunk)
        fout.close()
    except:
        print "no file !"
def getDimensions( image ):
    img=cv2.imread(image,0)
    if((img is not None) and img.any()):
        global IMAGE_AVAILABLE
        IMAGE_AVAILABLE=True
        # print img
        height, width = img.shape
        dimensions ={'image':image, 'height': height, 'width': width}
        dumped=json.dumps(dimensions)
        print
        print dumped

    else:
        print "no image uploaded"

def delete (image):
    if(IMAGE_AVAILABLE):
        os.remove(image)

save_uploaded_file ("file_1", UPLOAD_DIR)
print_html_form ()
getDimensions(IMAGE)
get_landmarks.get_landmarks(IMAGE)
delete(IMAGE)

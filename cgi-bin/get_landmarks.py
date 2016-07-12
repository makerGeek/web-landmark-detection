#!/usr/bin/python
# The contents of this file are in the public domain. See LICENSE_FOR_EXAMPLE_PROGRAMS.txt
#
#   This example program shows how to find frontal human faces in an image and
#   estimate their pose.  The pose takes the form of 68 landmarks.  These are
#   points on the face such as the corners of the mouth, along the eyebrows, on
#   the eyes, and so forth.
#
#   This face detector is made using the classic Histogram of Oriented
#   Gradients (HOG) feature combined with a linear classifier, an image pyramid,
#   and sliding window detection scheme.  The pose estimator was created by
#   using dlib's implementation of the paper:
#      One Millisecond Face Alignment with an Ensemble of Regression Trees by
#      Vahid Kazemi and Josephine Sullivan, CVPR 2014
#   and was trained on the iBUG 300-W face landmark dataset.
#
#   Also, note that you can train your own models using dlib's machine learning
#   tools. See train_shape_predictor.py to see an example.
#
#   You can get the shape_predictor_68_face_landmarks.dat file from:
#   http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
#
# COMPILING/INSTALLING THE DLIB PYTHON INTERFACE
#   You can install dlib using the command:
#       pip install dlib
#
#   Alternatively, if you want to compile dlib yourself then go into the dlib
#   root folder and run:
#       python setup.py install
#   or
#       python setup.py install --yes USE_AVX_INSTRUCTIONS
#   if you have a CPU that supports AVX instructions, since this makes some
#   things run faster.
#
#   Compiling dlib should work on any operating system so long as you have
#   CMake and boost-python installed.  On Ubuntu, this can be done easily by
#   running the command:
#       sudo apt-get install libboost-python-dev cmake
#
#   Also note that this example requires scikit-image which can be installed
#   via the command:
#       pip install scikit-image
#   Or downloaded from http://scikit-image.org/download.html.

import sys
import os , cgi
import dlib
import glob
from skimage import io

# if len(sys.argv) != 2:
#     print
#     print(
#         "Insufficient arguments "
#         "Give the path to the image files'folder.\n"
#         "For example, if you are in the python_examples folder then "
#         "execute this program by running:\n"
#         "    ./face_landmark_detection.py ../examples/faces\n")
#     exit()


def get_landmarks(filename):
    try:
        predictor_path = "dat\\shape_predictor_68_face_landmarks.dat"
        img_file= filename

        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(predictor_path)
        # win = dlib.image_window()

        # print("Processing file: {}".format(img_file))
        img = io.imread(img_file)

        # win.clear_overlay()
        # win.set_image(img)

        # Ask the detector to find the bounding boxes of each face. The 1 in the
        # second argument indicates that we should upsample the image 1 time. This
        # will make everything bigger and allow us to detect more faces.
        dets = detector(img, 1)

        #the format of the JSON is as follows:
        #     {
        #    "faces_count":2,
        #    "faces":[
        #       {
        #          "parts_count":3,
        #          "x":[
        #             1,
        #             2,
        #             3
        #          ],
        #          "y":[
        #             98,
        #             113,
        #             127
        #          ]
        #       },
        #       {
        #          "parts_count":3,
        #          "x":[
        #             1,
        #             2,
        #             3
        #          ],
        #          "y":[
        #             98,
        #             113,
        #             127
        #          ]
        #       }
        #    ]
        # }
         #beginning JSON {
        print "{"
        if(len(dets)==0):
                print('"faces_count": 0 }')
        else:
            print('"faces_count": {}, '.format(len(dets)))
            #opened faces array [
            print('"faces":[')
            #for each face we detected
            for k, d in enumerate(dets):
                #beginning of face :
                print "{"
                # print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                #     k, d.left(), d.top(), d.right(), d.bottom()))
                # Get the landmarks/parts for the face in box d.
                shape = predictor(img, d)
                #print the number of landmark points
                print ('"parts_count": {}, '.format(shape.num_parts))
                #print the x coordinate of each point
                print '"x" : ['
                for i in range(0, shape.num_parts):
                    print (shape.part(i).x)
                    if(i+1!=shape.num_parts):
                        print ", "
                print "], "

                #print the y coordinate of each point
                print '"y" : ['
                for i in range(0, shape.num_parts):
                    print (shape.part(i).y)
                    if(i+1!=shape.num_parts):
                        print ", "
                print "]"

                #end of face
                print "}"
                if(k!=len(dets)-1):
                    print ", "
                else:
                    #end of faces array
                    print "]"
                # Draw the face landmarks on the screen.
                # win.add_overlay(shape)
            #end of all JSON
            print "}"

            # win.add_overlay(dets)
            # dlib.hit_enter_to_continue()
    except:
        print "<br>must have argument image"
        print "<br>filename : " + filename

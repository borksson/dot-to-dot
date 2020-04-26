#Python 3

# coding: utf-8

# Import required libraries
import numpy as np
import cv2
from ImgResize import *
from ShowImage import *

#IDENTIFY CIRCLES

#Define image path
inImage = "_assets/dtd.png"
# Load in color image in grayscale
img = cv2.imread(inImage,0)
#img = imgResize(img, 20)
showImage(img)
# Creates an images with thresed values
ret,thresh=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
edges=cv2.Canny(thresh,100,200)
# Show image
showImage(edges)
# Identify and outline circles
cimg = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
minDist = 20
param1 = 100
param2 = 10
minRadius = 4
maxRadius = 5
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist,
                            param1=param1,param2=param2,minRadius=minRadius,maxRadius=maxRadius)
if circles is not None:
    print(circles, len(circles[0]) )
    for i in circles[0,:]:
        # draw the outer circle
        if(i[2]>=0):
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)
        # draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    showImage(cimg)
else:
    print("No circles")
    minDist-=1
# Show image

#IDENTIFY NUMBERS

#Make masks
masks = []
w = 17
h = 10
for i in circles[0,:]:
    x,y,r = int(i[0]),int(i[1]),int(i[2])
    test=np.ones_like(img)
    cv2.rectangle(test,((x-r),(y-r-h)),((x+r+w),(y+r)),(255,255,255),-1)
    #apply mask
    roi=cv2.bitwise_and(test,img)
    masks.append(roi)
for i in masks:
    if i is masks[0]:
        masterRois = i
    else:
        masterRois = cv2.add(masterRois, i)
showImage(masterRois)

#Train dataset

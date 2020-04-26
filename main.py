#Python 3

# coding: utf-8

# Import required libraries
import numpy as np
import cv2
from ImgResize import *
from ShowImage import *
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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
    splitMasks = []
    #FIXME: Crop instead of off image
    #Main mask
    test=np.ones_like(img)
    cv2.rectangle(test,((x-r),(y-r-h)),((x+r+w),(y+r)),(255,255,255),-1)
    oRoi=cv2.bitwise_and(test,img)
    #showImage(oRoi)
    #Num1
    test=np.ones_like(img)
    cv2.rectangle(test,((x-r+10),(y-r-h)),((x+r+w-8),(y+r)),(255,255,255),-1)
    roi=cv2.bitwise_and(test,img)
    #showImage(roi)
    splitMasks.append(roi)
    #Num2
    test=np.ones_like(img)
    cv2.rectangle(test,((x-r+18),(y-r-h)),((x+r+w),(y+r)),(255,255,255),-1)
    roi=cv2.bitwise_and(test,img)
    if np.mean(roi) != 255:
        print('Not all white')
        #showImage(roi)
        splitMasks.append(roi)
    masks.append([oRoi,splitMasks])

#Seperate numbers
showImage(masks[0][0])
i = circles[0][0]
x,y,r = int(i[0]),int(i[1]),int(i[2])
masks[0] = [masks[0],[]]
splitMasks = masks[0][1]
test=np.ones_like(img)
cv2.rectangle(test,((x-r+10),(y-r-h)),((x+r+w-8),(y+r)),(255,255,255),-1)
#showImage(roi)
test=np.ones_like(img)
cv2.rectangle(test,((x-r+18),(y-r-h)),((x+r+w),(y+r)),(255,255,255),-1)
roi=cv2.bitwise_and(test,img)
#showImage(roi)

#OCR
img_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_rgb))

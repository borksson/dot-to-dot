
# coding: utf-8

# importing
import cv2
# defines showImage
def showImage(img):
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# defines image path
imgPath = "_assets/black_circles.png"
# Load an color image in grayscale
src = cv2.imread(imgPath,0)
myTuple = (255,330)
# resizes image
img = cv2.resize(src, myTuple)
# showImage
showImage(img)

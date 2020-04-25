# coding: utf-8

# importing
import cv2
# defines showImage
def showImage(img):
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#Defines Image Resize
def imgResize(src, scale_percent):
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(src, dim)
# defines image path
imgPath = "_assets/black_circles.png"
# Load an color image in grayscale
src = cv2.imread(imgPath,0)
img = imgResize(src, 20)
showImage(img)

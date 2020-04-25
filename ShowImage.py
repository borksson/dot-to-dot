# coding: utf-8
from cv2 import imshow, waitKey, destroyAllWindows
#Defines Image Resize
def showImage(img):
    imshow('image',img)
    waitKey(0)
    destroyAllWindows()
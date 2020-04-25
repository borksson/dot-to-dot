# coding: utf-8
from cv2 import resize
#Defines Image Resize
def imgResize(src, scale_percent):
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)
    dim = (width, height)
    return resize(src, dim)

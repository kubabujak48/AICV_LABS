import cv2 as cv
import numpy as np
from random import randrange



def edging(img):
    scale = 1
    delta = 0
    depth = cv.CV_16S
    grad_x = cv.Sobel(img, depth, 1, 0, ksize=5, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(img, depth, 0, 1, ksize=5, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    return grad



#########################################################



# Load images
img1 = cv.imread('lena.png', 0)
img2 = cv.imread('pic.png', 0)

# Copy one of the images (select one)
img = img1.copy()
#img = img2.copy()


cv.imshow('Original image', img)

#Detecting the edge
edge_img = edging(img)
cv.imshow('Image with detected edges', edge_img)

cv.waitKey()
cv.destroyAllWindows()
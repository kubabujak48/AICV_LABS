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

def edging_1(img):
        kernel_sharpening = np.array([[-1, -1, -1],
                                      [-1, 9, -1],
                                      [-1, -1, -1]])
        sharpened = cv.filter2D(img, -1, kernel_sharpening)

        return sharpened


def edging_2(img):
        kernel_sharpening = np.array([[-1, -1, -1],
                                      [-1, 12, -1],
                                      [-1, -1, -1]])
        sharpened = cv.filter2D(img, -1, kernel_sharpening)

        return sharpened



#########################################################




# Load image
#img = cv.imread('lena.png', 0)
img = cv.imread('pic.jpg', 0)


cv.imshow('Base image', img)

#Detecting the edge

e1 = edging_1(img)
cv.imshow('Laplace 1', e1)

e2 = edging_2(img)
cv.imshow('Laplace 2', e2)

e_s = edging(img)
cv.imshow('Sobel', e_s)

cv.waitKey()
cv.destroyAllWindows()
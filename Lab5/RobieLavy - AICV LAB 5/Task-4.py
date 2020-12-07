import cv2 as cv
import numpy as np
from random import randrange


def noise(img):
    sr =  0
    dv = 4
    gaussian_noise = np.zeros(img.shape)
    x = cv.randn(gaussian_noise, sr, dv)
    gaussian_noise = np.uint8(gaussian_noise)
    output = cv.addWeighted(img, 0.5, gaussian_noise, 0.5, 0)

    return output

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




# Load image
img = cv.imread('lena.png', 0)
#img = cv.imread('pic.jpg', 0)


cv.imshow('Base image', img)

#Adding Gaussian noise
img_noisy = noise(img)
cv.imshow('Noisy image', img_noisy)

#Detecting the edge
edge_img = edging(img)
cv.imshow('Image with detected edges', edge_img)

cv.waitKey()
cv.destroyAllWindows()

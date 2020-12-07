import cv2 as cv
import numpy as np
from random import randrange


def noise(img):
    sr =  0
    dv = 4
    gaussian_noise = np.zeros(img.shape)
    x = cv.randn(gaussian_noise, sr, dv)
    gaussian_noise = np.uint8(gaussian_noise)
    output = cv.addWeighted(img, 1, gaussian_noise, 1, 0)

    return output

def gaussian_filter(img):
    blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

    return blur

def kernel_sharp(img):
    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    sharpened = cv.filter2D(img, -1, kernel_sharpening)

    return sharpened



##########################################################



# Load images
img1 = cv.imread('lena.png', 0)
img2 = cv.imread('pic.jpg', 0)

# Copy one of the images (select one)
#img = img1.copy()
img = img2.copy()

cv.imshow('Original image', img)

# Adding Gaussian noise to image
img_with_noise = noise(img)
cv.imshow('Image noise', img_with_noise)

#Removing noise
img_filter = gaussian_filter(img)
cv.imshow('Gaussian filtering', img_filter)

#Sharpening the picture
img_sharp = kernel_sharp(img_filter)
cv.imshow('Sharp', img_sharp)

cv.waitKey()
cv.destroyAllWindows()





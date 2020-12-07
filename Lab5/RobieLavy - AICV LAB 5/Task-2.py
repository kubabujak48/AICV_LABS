import cv2 as cv
import numpy as np
from random import randrange



def noise(img):
    s = salt(img)
    p = pepper(img)
    noise = cv.addWeighted(s, 0.5, p, 0.5, 0)
    output = cv.addWeighted(img, 0.5, noise, 0.5, 0)

    return output

def salt(img):
    rows, cols = img.shape[:2]
    dens = (rows*cols*0.5)//2
    dens = int(dens)

    print(dens)

    for d in range(0, dens):
        x = randrange(rows)
        y = randrange(cols)
        img[x, y] = 255

    return img

def pepper(img):
    rows, cols = img.shape[:2]
    dens = (rows * cols * 0.2)//2
    dens = int(dens)

    print(dens)

    for d in range(0, dens):
        x = randrange(rows)
        y = randrange(cols)
        img[x, y] = 0

    return img

def filter(img):
    blur = cv.medianBlur(img, 3)

    return blur

def kernel_sharp(img):
    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    sharpened = cv.filter2D(img, -1, kernel_sharpening)

    return sharpened



#########################################################



# Load images
img1 = cv.imread('lena.png', 0)
img2 = cv.imread('pic.png', 0)

# Copy one of the images (select one)
img = img1.copy()
#img = img2.copy()


cv.imshow('Original image', img)

# Adding S&P noise to image
img_with_noise = noise(img)
cv.imshow('Image noise', img_with_noise)

#Removing noise
img_filter = filter(img)
cv.imshow('Image median filtering', img_filter)

#Sharpening the picture
img_sharp = kernel_sharp(img_filter)
cv.imshow('Sharp', img_sharp)

cv.waitKey()
cv.destroyAllWindows()
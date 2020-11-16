import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# Function displaying the image
def print_img(temp, name):
    cv.imshow(name, temp)
    cv.waitKey(0)
    cv.destroyAllWindows()


# Function making the histogram of image
def make_histogram(filename, file):
    cv.imshow(filename, file)  # show current image
    plt.hist(file.ravel(), 256, [0, 256])
    plt.title('The histogram of ' + filename, fontdict=None, loc='center', pad=None)  # title for histogram
    plt.show()  # plotting histogram
    cv.waitKey(0)
    cv.destroyAllWindows()


# Function presenting the histogram of image
def equalize_histogram(filename, file):
    img_output = cv.cvtColor(file, cv.COLOR_BGR2LAB)  # black and white colours of the histogram
    eql = cv.equalizeHist(img_output, None)
    cv.imshow('Black&white histogram of ' + filename, img_output)

    make_histogram('Equalized histogram of ' + filename, eql)  # equalized histogram


# Function responsible for quantization of image
def quantize_image(filename, level=32):
    quant_out = np.zeros((filename.shape[0], filename.shape[1]), dtype='uint8')
    max = np.max(filename)
    min = np.min(filename)

    difference = (max - min) // level
    temp = 0

    for x in range(filename.shape[0]):
        for y in range(filename.shape[1]):
            quant_out[x, y] = filename[x, y]
            while True:
                if quant_out[x, y] <= min + difference or temp >= level:
                    break
                else:
                    quant_out[x, y] = quant_out[x, y] - difference
                    temp += 1
            quant_out[x, y] = temp * difference + min + difference // 2
            temp = 0
    return quant_out


def thresholding(img, type, title):
    ret, thresh = cv.threshold(img, 127, 255, type)
    make_histogram(title, thresh)


def DFT(img):
    img = cv.imread('lena.png', 0)
    img_float32 = np.float32(img)
    make_dft = cv.dft(img_float32, flags=cv.DFT_COMPLEX_OUTPUT)
    shift_dft = np.fft.fftshift(make_dft)  # Shift of the zero frequency component to the centre of spectrum
    spec_mag = 20 * np.log(cv.magnitude(shift_dft[:, :, 0], shift_dft[:, :, 1]) + 1)

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(spec_mag, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()


def inverse_DFT(img):
    rows, cols = img.shape
    crow, ccol = rows / 2, cols / 2

    img_float32 = np.float32(img)
    make_dft = cv.dft(img_float32, flags=cv.DFT_COMPLEX_OUTPUT)
    shift_dft = np.fft.fftshift(make_dft)  # Shift of the zero frequency component to the centre of spectrum

    tmp = np.zeros((rows, cols, 2), np.uint8)
    tmp[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1

    phshift = shift_dft * tmp
    inv_phshift = np.fft.ifftshift(phshift)
    img_back = cv.idft(inv_phshift)
    img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img_back, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()


'''
make_histogram('Quant High - Level of Intensity: 32', quantize_image(img_high, 32))
make_histogram('Quant Low - Level of Intensity: 32', quantize_image(img_low, 32))

make_histogram('Quant High - Level of Intensity: 64', quantize_image(img_high, 64))
make_histogram('Quant Low - Level of Intensity: 64', quantize_image(img_low, 64))

make_histogram('Quant High - Level of Intensity: 128', quantize_image(img_high, 128))
make_histogram('Quant Low - Level of Intensity: 128', quantize_image(img_low, 128))

DFT(img_lena_nocol)
inverse_DFT(img_lena_nocol)
'''


def main():
    # Images paths definitions
    path_low = 'img_low.jpg'
    path_high = 'img_high.jpg'
    path_lena = 'lena.png'

    # LOADING UP IMAGES
    img_low = cv.imread(path_low, 0)
    img_high = cv.imread(path_high, 0)
    img_lena = cv.imread(path_lena, 1)
    img_lena_nocol = cv.imread(path_lena, 0)

    DFT(img_lena_nocol) # Run in scientific mode!!!

    make_histogram('High', img_high)
    make_histogram('Low', img_low)

    thresholding(img_lena, cv.THRESH_BINARY, 'Binary')
    thresholding(img_lena, cv.THRESH_BINARY_INV, 'Inverted Binary')


if __name__ == "__main__":
    main()

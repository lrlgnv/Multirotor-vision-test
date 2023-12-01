import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from scipy.ndimage import convolve

#https://lindevs.com/apply-gamma-correction-to-an-image-using-opencv

def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)

img = cv2.imread('blue.png')
gammaImg =(gammaCorrection(img, 2.7))
plt.imshow(gammaImg, cmap='gray')
plt.show()
plt.imshow(img, cmap='gray')
plt.show()
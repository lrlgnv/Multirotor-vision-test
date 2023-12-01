import cv2
import numpy as np

#https://lindevs.com/apply-gamma-correction-to-an-image-using-opencv

def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)

#gamma = float(input("Enter gamma value: "))
img = cv2.imread('blue.jpg')
gammaImg =(gammaCorrection(img, 2.2))
cv2.imshow('Orignal image', img)
cv2.imshow('Gamma corrected image', gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

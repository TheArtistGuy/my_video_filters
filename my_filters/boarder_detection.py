import cv2
import numpy as np

def picture_difference(img1, img2):
    matrix_dif = np.add(img1, np.multiply(img2, -1)) ** 2
    threshold_indizes = matrix_dif < 40
    matrix_dif[threshold_indizes] = 0
    return  matrix_dif


def gauss(img):
    img_2 = np.zeros_like(img)
    cv2.GaussianBlur(img, ksize=(7,7), sigmaX=4, dst=img_2)
    return np.add(img, np.multiply(img_2, -1)) ** 2

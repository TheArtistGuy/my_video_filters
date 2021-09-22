import cv2
import numpy as np

def picture_difference(img1, img2):
    return  np.add(img1,np.multiply(img2, -1)) ** 2


def gauss(img):
    img_2 = np.zeros_like(img)
    cv2.GaussianBlur(img, ksize=(7,7), sigmaX=4, dst=img_2)
    return np.add(img, np.multiply(img_2, -1)) ** 2
import numpy as np

def gauss(img1, img2):
    return  np.add(img1,np.multiply(img2, -1)) ** 2
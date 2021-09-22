import numpy as np

def echo_with_alpha(img_list: []):
    new_image = np.zeros_like(img_list[0])
    for i, picture in enumerate(img_list):
        alpha = 0.5 * (i)
        img = picture
        mask = np.full(img.shape, alpha)
        img = np.multiply(img, mask)
        new_image = np.add(new_image, img)

    return new_image / 8000


def echo(img_list : []):
    new_image = np.zeros_like(img_list[0])
    length = len(img_list)
    for picture in img_list:
        normalised_image = np.multiply(picture, (1/255) / length)
        new_image = np.add(new_image, normalised_image)

    return np.multiply(new_image, 1)
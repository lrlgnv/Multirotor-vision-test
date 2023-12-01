import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2

img = mpimg.imread("floor/yellow2.jpg")


# white balances an image based on a portion of the image that is expected to be white
# the white portion is decided from row, col, row_length, col_length
def white_balance(image, row, col, row_length, col_length):
    white_section = image[row : row + row_length, col : col + col_length]
    color_ratio = 255 / white_section[len(white_section) - 1, 0]
    white_balanced_image = np.copy(image)
    white_balanced_image = ((white_balanced_image * color_ratio).astype(int)).clip(
        0, 255
    )

    plt.imshow(white_balanced_image, cmap="gray")
    plt.title("White Balanced Image")
    plt.show()


if __name__ == "__main__":
    plt.imshow(img, cmap="gray")
    plt.title("Original Image")
    plt.show()
    white_balance(img, len(img) - 101, 0, 100, 100)

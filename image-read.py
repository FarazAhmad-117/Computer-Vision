# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:50:08 2025

@author: dell
"""

import cv2


#  How to read an image
# img1 = cv2.imread("./image-sample1.webp")


# How to display an image
# cv2.imshow("Image 1", img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# How to resize an image
# img2 = cv2.resize(img1, (1180, 600))  # width, height
# cv2.imshow("New resized image", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# How to show an image in grayscale
# img = cv2.imread("./image-sample1.webp", 0)
# cv2.imshow("Orginal", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Write a program to take an image in the current directory and save its gray scale to an output location
imageName = input("Enter image name:")

img = cv2.imread(f"./{imageName}", 0)

outputName = "gray_" + imageName

cv2.imwrite(f"./output/{outputName}", img)

cv2.imshow("Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

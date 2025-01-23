# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:50:08 2025

@author: dell
"""

import cv2

img1 = cv2.imread("./image-sample1.webp")

cv2.imshow("Image 1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
"""
ROI
Created on Wed Aug 23 16:00:32 2017

@author: Cho
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.morphology import thin

img = cv2.imread('line.jpg', 0)
_, th = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
bn = np.zeros_like(img)
skel = thin(th)
bn[skel] = 255

roi_R = 40
roi_C = 40
for r in range(roi_R, bn.shape[0]-roi_R):
    for c in range(roi_C, bn.shape[1]-roi_C):
        if skel[r, c]:
            # plt.imshow(bn[r-roi_R:r+roi_R, c-roi_C:c+roi_C])
            cv2.rectangle(img,(c-roi_C,r-roi_R),(c+roi_C,r+roi_R),(128),3)
            skel[r-roi_R:r+roi_R, c-roi_C:c+roi_C] = False

plt.imshow(img)
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:19:48 2017

@author: Cho
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# 이미지 불러오기
img = cv2.imread('burst.png', 0)

# 임계화
_, th = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)  
# 라벨링
num, L_img, L, _ = cv2.connectedComponentsWithStats(th)

# 라벨별로 저장 
for n in range(1, num):
    if L[n][-1] > 100:
        c0, r0 = L[n][0], L[n][1]
        c1, r1 = c0+L[n][2], r0+L[n][3]
        tmp = L_img[r0:r1, c0:c1].copy()
        obj = np.zeros_like(tmp)
        obj[tmp == n] = 255
        plt.imshow(obj, 'gray')
        plt.show()

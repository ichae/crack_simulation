# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 13:31:15 2017

@author: USER
"""

import cv2
import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt

img = np.zeros((100,100), np.int32)

a = randint(20,40, size=1)
b = randint(20,70, size=1)
c = randint(60,80, size=1)
d = randint(20,70, size=1)

pts = np.array([[99,0], [c,d], [a,b], [0,99]], np.int32) 
pts = pts.reshape((-1, 1, 2))

img = cv2.polylines(img, [pts], False, 255)


plt.imshow(img)
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:52:56 2017

@author: USER
"""

from skimage.draw import line
import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt

img = np.zeros((10, 10), dtype=np.uint8)
r = np.random.randint(10, size=2)
c = np.random.randint(10, size=2)

rr, cc = line(1, 1, 8, 8)
img[rr, cc] = 1


img[r, c] = 1   

#%%
from skimage.draw import line
import numpy as np
from numpy.random import randint

img = np.zeros((50,50), dtype=np.uint8)
r = randint(25, size=1)
c = randint(50, size=1)

#%%
tree = line(25, 25, 0, c)
tree2 = line(25, 25, 0, r)
rr, cc = line(49, 25, 25, 25)
img[rr, cc] = 1
img[tree] = 1
img[tree2] = 1

plt.imshow(img)
plt.show()

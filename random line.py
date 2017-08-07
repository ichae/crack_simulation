# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 09:27:27 2017

@author: USER
"""

from skimage.draw import line
import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt

img = np.zeros((500,500), dtype=np.uint8)

r = randint(0,499 , size=1)[0]
c = randint(0,499 , size=1)[0]
a = randint(0,499 , size=1)[0]
b = randint(0,499 , size=1)[0]
if c<b:
    d = randint(c,b , size=1)[0]
else :
    d = randint(b,c , size=1)[0]
if r<a:
    e = randint(r,a , size=1)[0]
else :
    e = randint(a,r , size=1)[0]
tree = line(r,c,e,d)
tree2 = line(e,d,a,b)
img[tree] = 1
img[tree2] = 1
    





plt.imshow(img)
plt.show()
    

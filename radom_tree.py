# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:52:56 2017

@author: USER
"""

#%%
from skimage.draw import line
import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt


img = np.zeros((150,150), dtype=np.uint8)
r = randint(50,60 , size=1)[0]
c = randint(90,100 , size=1)[0]
s = randint(70,80 , size=1)[0]

#%%
tree = line(100, 75, s, c)
tree2 = line(100, 75, s, r)
rr, cc = line(149, 75, 100, 75)
img[rr, cc] = 1
img[tree] = 1
img[tree2] = 1

number = [1,1]
for i in number:
    a = randint(0,30 , size=1)[0]
    b = randint(-10,30 , size=1)[0]
    tree3 = line(s, c, s-a*i, c+b*i)
    d = randint(0,30 , size=1)[0]
    e = randint(-10,30 , size=1)[0]
    tree4 = line(s-a*i, c+b*i,  s-a*i-d, c+b*i+e)
   
    img[tree3] = 1
    img[tree4] = 1
    
for i in number:
    a = randint(0,30 , size=1)[0]
    b = randint(-10,30 , size=1)[0]
    tree3 = line(s, r, s-a*i, r-b*i)
    d = randint(0,30 , size=1)[0]
    e = randint(-10,30 , size=1)[0]
    tree4 = line(s-a*i, r-b*i,  s-a*i-d, r-b*i-e)
    img[tree3] = 1
    img[tree4] = 1
  

plt.imshow(img)
plt.show()

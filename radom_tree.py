#%%
from skimage.draw import line
import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt

img = np.zeros((200,200), dtype=np.uint32)
rr,cc = line(199,100,150,100)
img[rr,cc] = 1
a = randint(100,120,size=1)[0]
b = randint(120,130,size=1)[0]
tree = line(150,100,a,b)
img[tree] = 1
c = randint(70,80, size=1)[0]
tree2 = line(150,100,a,c)
img[tree2] = 1

d = randint(-9,9, size=1)[0]
e = randint(10,35, size=1)[0]
tree3 = line(a,c,a+d,c-e)
if e<20:
    img[tree3] = 0
else:
    img[tree3] = 1
    for i in [-1,1]:    
        f = randint(19,33, size=1)[0]
        g = randint(10,34, size=1)[0]
        tree7 = line(a+d,c-e,a+d+f*i,c-e-g)
        if g<20:
            img[tree7] = 0
        else:
            img[tree7] = 1
            
d = randint(-9,9, size=1)[0]
e = randint(10,35, size=1)[0]
tree4 = line(a,c,a-e,c+d)
if e<20:
    img[tree4] = 0
else:
    img[tree4] = 1
    for i in [-1,1]:
        f = randint(19,33, size=1)[0]
        g = randint(10,34, size=1)[0]
        tree8 = line(a-e,c+d,a-e-f,c+d+g*i)
        if g<20:
            img[tree8] = 0
        else:
            img[tree8] = 1
            
d = randint(-9,9, size=1)[0]
e = randint(10,35, size=1)[0]
tree5 = line(a,b,a+d,b+e)
if e<20:
    img[tree5] = 0
else:
    img[tree5] = 1
    for i in [-1,1]:    
        f = randint(19,33, size=1)[0]
        g = randint(10,34, size=1)[0]
        tree9 = line(a+d,b+e,a+d+f*i,b+e+g)
        if g<20:
            img[tree9] = 0
        else:
            img[tree9] = 1
            
d = randint(-9,9, size=1)[0]
e = randint(10,35, size=1)[0]
tree6 = line(a,b,a-e,b+d)
if e<20:
    img[tree6] = 0
else:
    img[tree6] = 1
    for i in [-1,1]:
        f = randint(19,33, size=1)[0]
        g = randint(10,34, size=1)[0]
        tree10 = line(a-e,b+d,a-e-f,b+d+g*i)
        if g<20:
            img[tree10] = 0
        else:
            img[tree10] = 1
            
plt.imshow(img)
plt.show()

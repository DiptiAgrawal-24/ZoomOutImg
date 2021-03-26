# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:21:34 2021

@author: Dipti
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open("pic.jpg")
print(image.format)
print(image.size)
print(image.mode)

np_img = np.array(image)
print(np_img)
print(np_img.shape)
gray_data = np_img[:,:,0]
print(gray_data.shape)

w , h = gray_data.shape
print("Width:{}\tHeight:{}".format(w,h))

xNew = int(w * 1/2)
yNew = int(h * 1/2)

xscale = xNew/(w-1)
yscale = yNew/(h-1)
print("New Image: ")
newImg = np.zeros([xNew + 1, yNew +1]) 

for i in range(0,xNew - 1):
    for j in range(0, yNew - 1):
        newImg[i+1, j+1] = gray_data[1 + int(i/xscale), 1 + int(j/yscale)]
print(newImg.shape)
plt.imshow(newImg,cmap = "gray")
plt.show()
 
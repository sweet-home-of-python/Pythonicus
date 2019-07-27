import os
from PIL import Image, ImageOps
import numpy as np


import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def red_extractor(image):
    data = np.array(image)
    red, green, blue = data.T
    im2 = Image.fromarray(red.T)
    return im2


x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()



imagePath = "line_finder\\images\\red.JPG"


image = Image.open(imagePath)

img_Red = red_extractor(image)

imgarray = np.array(img_Red)

for line in imgarray:
    print(line) 

Image._show(img_Red)

#img_Red.save("line_finder\\iline.JPG")


from ImageProcessor import ImageProcessor
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ColorFilter():
    def invert(self, array):
        for i in array:
            for k in i:
                k[0] = 255 - k[0]
                k[1] = 255 - k[1]
                k[2] = 255 - k[2]
        
        return array


    def to_blue(self, array):
        for i in array:
            for k in i:
                k[0] = 0
                k[1] = 0

        return array
 
    def to_green(self, array):
        for i in array:
            for k in i:
                k[0] = 0
                k[2] = 0

        return array

    def to_red(self, array):
        for i in array:
            for k in i:
                k[1] = 0
                k[2] = 0

        return array

    def celluloid(self, array):
        pass

merapi = ImageProcessor()

array = merapi.load("merapi.jpeg")

test = ColorFilter()

crp = test.invert(array)
crp_plot = plt.imshow(crp)
plt.show()

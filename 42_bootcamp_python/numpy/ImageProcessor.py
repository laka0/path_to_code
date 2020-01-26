import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ImageProcessor():
    def load(self, path):
        pic = mpimg.imread(path)
        height = format(pic.shape[0])
        width = format(pic.shape[1])

        print("Height: %s\nWidth: %s" % (height, width))
        
        array = np.array(pic)
        return array

    def display(self, array):
        imgplot = plt.imshow(array)
        plt.show()

        return imgplot


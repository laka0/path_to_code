import ImageProcessor
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ScrapBooker():
    def crop(self, array, dimensions, position = (0, 0)):
        while dimensions[0] > len(array) or dimensions[1] > len(array[0]):
            print("Error, cropped dimensions are superior to image size")
            dimensions = input("Enter a new dimensions tuple below\n")
        
        cropped_array = array[position[0]:dimensions[0], position[1]:dimensions[1]]

        return cropped_array


    def thin(self, array, n, axis):
        thin_arr = np.delete(array, np.s_[::n], axis)
        print(len(thin_arr))
        print(len(thin_arr[0]))
        return thin_arr


    def juxtapose(self, array, n, axis):
        new_arr = array 
        for i in range(n):
            new_arr = np.concatenate((new_arr, array), axis)

        return new_arr

    def mosaic(self, array, dimensions):
        new_arr = np.tile(A = array, reps = dimensions)

        return new_arr
        

merapi = ImageProcessor.ImageProcessor()

array = merapi.load("merapi.jpeg")
print(np.shape(array))

test = ScrapBooker()

crp = test.mosaic(array, (4, 2, 1))
crp_plot = plt.imshow(crp)
plt.show()

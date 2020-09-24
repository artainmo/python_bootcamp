import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

class ScrapBooker:
    def crop(self, array, dimensions, position=(0,0)): #crop the image as a rectangle with the given dimensions (mean- ing, the new height and width for the image), whose top left corner is given by the position argument. The position should be (0,0) by default. You have to consider it an error (and handle said error) if dimensions is larger than the current image size.
        if position[1] + dimensions[1] > array.shape[1] or position[0] + dimensions[0] > array.shape[0]:
            print(error)
        cropped = array[position[0]:position[0] + dimensions[0], position[1]:position[1] + dimensions[1]]
        return cropped

    def thin(self, array, n, axis): #delete every n-th pixel row along the specified axis (0 vertical, 1 horizontal), example below.
        vertical = 0
        horizontal = 1
        if axis == "vertical":
            cropped = numpy.delete(array, n, vertical)
        if axis == "horizontal":
            cropped = numpy.delete(array, n, horizontal)
        return cropped

    def juxtapose(self, array, n, axis): #juxtapose n copies of the image along the specified axis (0 vertical, 1 horizontal).
            new = []
            if axis == "vertical":
                for i in range(0:n):
                    new = np.concatenate((new, array), axis=0)
            if axis == "horizontal":
                for i in range(0:n):
                    new = np.concatenate((new, array), axis=1)
            return new

    def mosaic(self, array, dimensions): #make a grid with multiple copies of the array. The dimensions argument specifies the dimensions (meaning the height and width) of the grid (e.g. 2x3).
        for i in range(0,dimensions[0]):
            new = np.concatenate((new, array), axis=0)
        for i in range(0,dimensions[1]):
            new = np.concatenate((new, array), axis=1)
        return new

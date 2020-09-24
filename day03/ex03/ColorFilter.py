import numpy as np

class ColorFilter:

    def invert(self, array): #Takes a NumPy array of an image as an argument and returns an array with inverted color.Authorized function : None Authorized operator: -
        return 1 - array

    def to_blue(self, array): #Takes a NumPy array of an image as an argument and returns an array with a blue filter.Authorized function : .zeros, .shape Authorized operator: None
        while i < array.shape[0]:
            while l < array.shape[1]:
                array[i][l][2] = 1
                l += 1
            i += 1
        return array

    def to_green(self, array): #Takes a NumPy array of an image as an argument and returns an array with a green filter.Authorized function : None Authorized operator: *
        while i < len(array):
            while l < len(array[i]):
                array[i][l][1] = 1
                l += 1
            i += 1
        return array

    def to_red(self, array): #Takes a NumPy array of an image as an argument and returns an array with a red filter. Authorized function : green, blue.Authorized operator: -, +
        while i < array.shape[0]:
            while l < array.shape[1]:
                array[i][l][0] = 1
                l += 1
            i += 1
        return array

    def celluloid(self, array, tresholds): #Takes a NumPy array of an image as an argument, and returns an array with a celluloid shade filter. The celluloid filter must display at least four thresholds of shades. Be careful! You are not asked to apply black contour on the object here (you will have to, but later. . . ), you only have to work on the shades of your images. Authorized function: arange, linspace
        return array.arange(0, tresholds, 1)

    def grayscale(self, array, filter=(0.299, 0.587, 0.114)):
        while i < array.shape[1]:
            while l < array.shape[1]:
                array[i][l] = array[i][l] * filter
            i += 1
        l += 1

import numpy as np:

class AdvancedFilter:

    def get_sliced(self, array, kernel, pos, blur):
        first_row = array[0 + pos[0]][0 + pos[1]:kernel[1] + pos[1]]
        second_row = array[1 + pos[0]][0 + pos[1]:kernel[1] + pos[1]]
        third_row = array[2 + pos[0]][0 + pos[1]:kernel[1] + pos[1]]
        sliced = np.concatenate((first_row, second_row, third_row), axis=0)
        if blur == "gaussian":
            sliced[1][1] *= 4
            sliced[1][0] *= 2
            sliced[1][2] *= 2
            sliced[0][1] *= 2
            sliced[2][1] *= 2
            sliced[0][0] *= 1
            sliced[2][2] *= 1
            sliced[0][2] *= 1
            sliced[2][0] *= 1
        blur_value = np.sum(sliced) / (sliced.shape[0] * sliced.shape[1])
        return np.full(kernel, blur_value)

    def mean_blur(self, array): #This method receives an image, performs a mean blur on it and returns a blurred copy. In a mean blur, each pixel becomes the average of its neighboring pixels.
        kernel = (3,3)
        new = array
        for x in range(0:len(array):kernel[0])
            for y in range(0:len(array[0]):kernel[1])
                slice = self.get_sliced(array, kernel, (x, y), "mean")
                new = new.concatenate((new, slice), out=(x,y))
        return new

    def gaussian_blur(self, array): #This method receives an image, performs a gaussian blur on it and returns a blurred copy. In a gaussian blur, the weighting of the neighboring pixels is adjusted so that closer pixels are more heavily counted in the average.
        kernel = (3,3)
        new = array
        for x in range(0:len(array):kernel[0])
            for y in range(0:len(array[0]):kernel[1])
                slice = get_sliced(array, kernel, (x, y), "gaussian")
                new = new.concatenate((new, slice), out=(x,y))
        return new

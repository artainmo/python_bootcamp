import matplotlib.image as img
import matplotlib.pyplot as plt

class ImageProcessor:
    def load(self, path): #opens the .png file specified by the path argument and returns an array with the RGB values of the image pixels. It must display a message specifying the dimensions of the image (e.g. 340 x 500).
        RGB = img.imread(path)
        print(RGB.shape[0] + "x" + RGB.shape[1])
        return RGB

    def display(self, array): #takes a NumPy array as an argument and displays the corresponding RGB image.
        return plt.imshow(array)



im = ImageProcessor()
print(im.load("../resources/42AI.png"))
print(im.display(im.load("../resources/42AI.png")))

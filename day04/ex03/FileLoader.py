import os
import pandas as pd
from HowManyMedals import howManyMedals

class FileLoader:

    def load(path): #The argument of this method is the file path of the dataset to load. It must display a message specifying the dimensions of the dataset (e.g. 340 x 500). The method returns the dataset loaded as a pandas.DataFrame.
        i = len(path) - 1
        while path[i] != '.':
            i -= 1
        extension = path[i:len(path)]
        if extension == ".txt":
            file = pd.read_txt(path)
        if extension == ".csv":
            file = pd.read_csv(path)
        print("Loading dataset of dimensions %d x %d" % (file.shape[0], file.shape[1]))
        return file


    def display(df, n): #Takes a pandas.DataFrame and an integer as arguments. This method displays the first n rows of the dataset if n is positive, or the last n rows if n is negative.
        if n >= 0:
            print(df.iloc[0:n])
        else:
            print(df.iloc[n - 1:-1])


pan = FileLoader
file = pan.load(os.getcwd() + "/../resources/athlete_events.csv")
print(howManyMedals(file, "Piotr ya"))

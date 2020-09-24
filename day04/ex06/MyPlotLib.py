import pandas as pn
import seaborn as sns
import scipy
import matplotlib.pyplot

class MyPlotLib:
    def get_numerical_features(self, data, features):
        list = []
        for item in features:
            list.append(data[item].to_frame())
        return list

    def histogram(self, data, features): #plots one histogram for each numerical feature in the list
        list = self.get_numerical_features(data, features)
        for data in list:
            matplotlib.pyplot.show(pn.DataFrame.hist(data))

    def density(self, data, features): #plots the density curve of each numerical feature in the list
        list = self.get_numerical_features(data, features)
        for data in list:
            matplotlib.pyplot.show(sns.distplot(data))

    def pair_plot(self, data, features): #plots a matrix of subplots (also called scatter plot matrix). On each subplot shows a scatter plot of one numerical variable against another one. The main diagonal of this matrix shows simple histograms.
        list = self.get_numerical_features(data, features)
        for data in list:
            matplotlib.pyplot.show(pn.plotting.scatter_matrix(data))

    def box_plot(self, data, features): #displays a box plot for each numerical variable in the dataset.
        list = self.get_numerical_features(data, features)
        for data in list:
            matplotlib.pyplot.show(pn.DataFrame.boxplot(data))

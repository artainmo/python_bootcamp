import pandas as pn

class SpatioTemporalData:
    def __init__(self, panda_dataframe):
        self.pn = panda_dataframe

    def when(self, location): #This method takes a location as an argument and returns a list containing the years where games were held in the given location.
        location = self.pn[self.pn.City == location]
        location_unique_years = location.drop_duplicates(subset="Year", keep='first').Year
        return location_unique_years.tolist()



    def where(self, date): #This method takes a date as an argument and returns the location where the Olympics took place in the given year.
        city = self.pn[self.pn.Year == date].drop_duplicates(subset="City", keep='first').City
        return city.to_list()[0]

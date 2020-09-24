import pandas as pn

def proportionBySport(pn_dataframe, olympic_year, sport, gender):
    pn_dataframe = pn_dataframe.drop_duplicates(subset ="Name", keep = "first")
    demanded_dataframe = pn_dataframe[pn_dataframe.Sex == gender][pn_dataframe.Year == olympic_year][pn_dataframe.Sport == sport]
    return demanded_dataframe.shape[0] / pn_dataframe.shape[0]

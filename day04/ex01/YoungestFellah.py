import pandas as pd

def youngestFellah(panda_dataframe, olympic_year):
    olympic_year_male_candidates = panda_dataframe[panda_dataframe.Year == olympic_year][panda_dataframe.Sex == "M"]
    olympic_year_female_candidates = panda_dataframe[panda_dataframe.Year == olympic_year][panda_dataframe.Sex == "F"]
    youngest_male = olympic_year_male_candidates["Age"].idxmin()
    youngest_female = olympic_year_female_candidates["Age"].idxmin()
    return olympic_year_male_candidates.loc[youngest_male].to_dict(), olympic_year_female_candidates.loc[youngest_female].to_dict()

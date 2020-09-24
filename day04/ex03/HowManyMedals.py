import pandas

def howManyMedals(pn_dataframe, participant):
    dict = {}
    participant_index = pn_dataframe[pn_dataframe.Name == participant].index
    for i in participant_index:
        GSB = [0, 0, 0]
        if pn_dataframe.loc[i].Medal == "Gold":
            GSB[0] = 1
        if pn_dataframe.loc[i].Medal == "Silver":
            GSB[1] = 1
        if pn_dataframe.loc[i].Medal == "Bronze":
            GSB[2] = 1
        dict.update({pn_dataframe.loc[i].Year : {
        'G' : GSB[0],
        'S' : GSB[1],
        'B' : GSB[2]
        }})
    return dict

def howManyMedalsByCountry(pn_dataset, country):
    dict = {}
    country = pn_dataset[pn_dataset.Team == country]
    for year in country.Year:
        dict.update({
        year : {
        'G' : 0,
        'S' : 0,
        'B' : 0,
        }})
    for index, row in country.iterrows():
        if row.Medal == "Gold":
            dict[row.Year]["G"] += 1
        if row.Medal == "Silver":
            dict[row.Year]["S"] += 1
        if row.Medal == "Bronze":
            dict[row.Year]["B"] += 1
        return dict

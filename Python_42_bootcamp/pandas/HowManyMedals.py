from FileLoader import FileLoader

def howManyMedals(df, name):
    medals = {"Gold" : "G", "Silver" : "S", "Bronze" : "B"}
    how_many_medals = {}
    athlete_records = df.loc[df["Name"] == name]

    for index, row in athlete_records.iterrows():
        if row["Medal"] in medals:
            m = medals[row["Medal"]]

            if row["Year"] not in how_many_medals:
                how_many_medals.update({row["Year"] : {"G" : 0, "S":0, "B":0}})
                how_many_medals[row["Year"]][m] += 1
            
            else:
                how_many_medals[row["Year"]][m] += 1
        else:
            if row["Year"] not in how_many_medals:
                how_many_medals.update({row["Year"] : {"G" : 0, "S":0, "B":0}})

    
    return how_many_medals

loader = FileLoader()
data = loader.load("athlete_events.csv")

print(howManyMedals(data, "Kjetil Andr Aamodt"))


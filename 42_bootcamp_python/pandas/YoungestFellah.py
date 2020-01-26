from FileLoader import FileLoader

def youngestFellah(df, year):
    female_athlete = df.loc[(df["Sex"] == "F") & (df["Year"] == year)]
    male_athlete = df.loc[(df["Sex"] == "M") & (df["Year"] == year)]
    return {"Female: ": female_athlete["Age"].min(), "Male: ": male_athlete["Age"].min()}


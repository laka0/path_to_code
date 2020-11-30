from FileLoader import FileLoader

def proportionBySport(df, year, sport, gender):
    gender_total = df.loc[(df["Sex"] == gender) & (df["Year"] == year)]
    gender_shape = gender_total.shape

    sport_gender = gender_total.loc[gender_total["Sport"] == sport]
    sport_shape = sport_gender.shape

    return sport_shape[0]/gender_shape[0]

loader = FileLoader()

data = loader.load("athlete_events.csv")

print(proportionBySport(data, 2000, "Tennis", "F"))
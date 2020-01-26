from FileLoader import FileLoader

class SpatioTemporalData():
    def __init__(self, data):
        self.data = data
    
    def when(self, location):
        years = []
        rows = self.data.loc[self.data["City"] == location]
        
        for index, row in rows.iterrows():
            if row["Year"] not in years:
                years.append(row["Year"])
            
            else: 
                continue

        return years

    def where(self, date):
        location = []

        rows = self.data.loc[self.data["Year"] == date]
        location.append(rows.iloc[0]["City"])

        return location


loader = FileLoader()

data = loader.load("athlete_events.csv")

sp = SpatioTemporalData(data)
print(sp.where(1924))
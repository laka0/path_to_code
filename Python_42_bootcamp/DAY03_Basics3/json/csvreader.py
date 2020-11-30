from csv import reader

class CsvReader():
    def __init__(self, file, sep=",", header=False, skip_top=0, skip_bottom=0):
        while True:
            try:
                open(file)
                break
            except FileNotFoundError:
                file = input("This file does not exist.\nPlease enter a new path below\n")
    
        self.opened_file = open(file)
        self.read_file = reader(self.opened_file, delimiter = sep)
        self.l_file = list(self.read_file)

        for i in self.l_file:
            for k in range(len(i)):
                if len(i[k]) > 1000:
                    print("File is corrupted")

        if header == True:
            pass
        else:
            self.header = self.l_file[0]
            self.l_file.pop(0)
        
        if skip_top > 0:
            for i in range(skip_top):
                self.l_file.pop(0)
        else:
            pass

        if skip_bottom > 0:
            for i in range(skip_bottom):
                self.l_file.pop(-1)
        else: 
            pass

    def __enter__(self):
        return self.opened_file

    def __exit__(self, type, value, traceback):
        self.opened_file.close()
    
    def getdata(self):
        return self.l_file

    def getheader(self):
        return self.header
    
with CsvReader("ApplStore.csv") as file:
    file = CsvReader("AppleStore.csv")
    data = file.getdata()
    header = file.getheader()

    print(header)
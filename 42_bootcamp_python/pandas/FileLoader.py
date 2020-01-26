import pandas as pd 

class FileLoader():
    def load(self, path):
        load_file = pd.read_csv(path)
        shape = load_file.shape
        print("The dimensions of the dataframe are %sx%s" % (shape[0], shape[1]))

        return load_file

    def display(self, df, n):
        if n > 0:
            print(df.head(n))
        
        else:
            print(df.tail(n))


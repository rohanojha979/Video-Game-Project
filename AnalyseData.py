import pandas as pd

class Analyse:

    def __init__(self, path = 'vgsales.csv'):
        self.df = pd.read_csv(path)
        self.cleanData()

    def cleanData(self):
        self.df.drop(columns=[self.df.columns[0]], inplace=True)

    def getCategories(self):
        return self.df.groupby('Platform').count().sort_values('Global_Sales')['Global_Sales'][::-1]
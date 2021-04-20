import pandas as pd

class Analyse:

    def __init__(self, path = 'vgsales.csv'):
        self.df = pd.read_csv(path)
        self.cleanData()

    def cleanData(self):
        self.df = df.drop(columns=['Rank'])
        self.df.rename(columns={ 'NA_Sales': 'America', 'EU_Sales': 'Europe', 'JP_Sales': 'Japan', 'Other_Sales' : 'Other', 'Global_Sales' : 'Global' }, inplace = True)

        self.df['Year'].fillna(0, inplace=True)
        self.df['Year'] = df['Year'].astype('int')

        self.df.set_index('Name', inplace=True)

    def getCategories(self):
        return self.df.groupby('Platform').count().sort_values('Global_Sales')['Global_Sales'][::-1]
import pandas as pd

class Analyse:

    def __init__(self, path = 'datasets/vgsales.csv'):
        self.df = pd.read_csv(path)
        self.cleanData()

    def cleanData(self):
        
        self.df.rename(columns={ 'NA_Sales': 'America', 'EU_Sales': 'Europe', 'JP_Sales': 'Japan', 'Other_Sales' : 'Other', 'Global_Sales' : 'Global' }, inplace = True)
        self.df.drop(columns=['Rank'])
        self.df.rename(columns={ 'NA_Sales': 'America', 'EU_Sales': 'Europe', 'JP_Sales': 'Japan', 'Other_Sales' : 'Other', 'Global_Sales' : 'Global' }, inplace = True)

        self.df['Year'].fillna(0, inplace=True)
        self.df['Year'] = self.df['Year'].astype('int')

        self.df.set_index('Name', inplace=True)
        
    
    def getDataset(self):
        return self.df.groupby('Publisher').count().sort_values('Genre')['Genre'][::-1].head(50).plot(kind='bar', figsize = (20, 7))

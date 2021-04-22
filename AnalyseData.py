import pandas as pd

class Analyse:

    def __init__(self, path = 'vgsales.csv'):
        self.df = pd.read_csv(path)
        self.cleanData()

    def cleanData(self):
        
        self.df.rename(columns={ 'NA_Sales': 'America', 'EU_Sales': 'Europe', 'JP_Sales': 'Japan', 'Other_Sales' : 'Other', 'Global_Sales' : 'Global' }, inplace = True)

    def getpublisher(self):
        return self.df.groupby('Publisher').count().sort_values('Genre')['Genre'][::-1].head(50).plot(kind='bar', figsize = (20, 7))

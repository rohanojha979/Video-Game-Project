import pandas as pd

class Analyse:

    def __init__(self, path = 'datasets/vgsales.csv'):
        self.df = pd.read_csv(path)
        self.cleanData()
        self.df_upd = self.df[self.df['year']!= 0]

    def cleanData(self):
        self.df.drop(columns=[self.df.columns[0]], inplace=True)
        self.df.columns = self.df.columns.str.lower()
        self.df['year'] = self.df['year'].fillna(0)
        self.df['publisher'] = self.df['publisher'].fillna('unknown')
        self.df['year'] = self.df[self.df['year'].notna()]['year'].astype('int64')
        self.df ['total_sales'] = (
                          self.df['na_sales'] + 
                          self.df['eu_sales'] + 
                          self.df['jp_sales'] + 
                          self.df['other_sales'])

    def getTopPublishersByCount(self, n):
        return self.df.groupby('publisher').count().sort_values('year', ascending=False)['year'].head(n)

    def getTopPublishersBySum(self, n):
        return self.df.groupby('publisher').sum().sort_values('global_sales', ascending = False)['global_sales'].head(n)

    def getTopPublishersBySumInRegion(self, n, region):
        return self.df.groupby('publisher').sum().sort_values(region, ascending = False)[region].head(n)

    def getTopGenresByCount(self):
        return self.df.groupby('genre').count().sort_values('year', ascending=False)['year']

    def getTopGenresBySum(self):
        return self.df.groupby('genre').sum().sort_values('global_sales', ascending = False)['global_sales']

    def getTopGenresByCountInRegion(self, region):
        return self.df.groupby('genre').count().sort_values(region, ascending = False)[region]

    def getTopGenresBySumInRegion(self, region):
        return self.df.groupby('genre').sum().sort_values(region, ascending = False)[region]

    def getGenres(self):
        return self.df['genre'].unique()

    def getDataframe(self):
        return self.df

    def getYearWiseRelease(self):
        return self.df.groupby('year').count()['genre'][1:]

    def getPlatform(self):
        return self.df_upd.groupby('platform')['total_sales'].sum().sort_values(ascending=True)

    def getRegion(self):
        return zip(['na_sales', 'eu_sales', 'jp_sales', 'other_sales'], ['North America', 'Europe', 'Japan', 'Other'])

import csv
import pandas as pd


class Preprocessing(object):
    
    def __init__(self, df):
        self.df_cp = df
        self.del_column()
        self.set_header(df)
        self.index = 0
        self.starting_year = 1995
        self.final_year = 2020
        del df
    
    
    def del_column(self):
        del self.df_cp['MM']
        del self.df_cp['coleta']
        return self.df_cp 
    
    
    def set_starting_year(self, year):
        self.starting_year = year
        
    
    def set_final_year(self, year):
        self.final_year = year + 1
    
    
    def set_header(self, df):
        self.df = pd.DataFrame(df.iloc[[0]])
    
    
    def query_year_and_label(self, year, label):
        return self.df_cp[(self.df_cp['YYYY'] == year) & (self.df_cp['class'] == label)]
    
    
    def list_to_df(self, df, label):
        df = (df.mean())
        swap = []
        
        for i in df:
            swap.append(i)
        swap.append(label)
        
        return swap
    
    
    def df_2_csv(self, path):
        self.df.to_csv(path, encoding='utf-8', index=False)  
        
    
    def new_df(self, year, label):
        season = self.query_year_and_label(year, label)
        season = self.list_to_df(season, label)
        
        self.df.loc[self.index] = season
        del season
        self.index += 1
        
        return self.df
        
        
    def export(self, label, path):
        for i in range(self.starting_year, self.final_year):
            for j in label:
                self.new_df(i, j)    
        self.df_2_csv(path)
        
        
    ''' Docs and Reference 
        * [query]
            (https://stackoverflow.com/questions/22591174/pandas-multiple-conditions-while-indexing-data-frame-unexpected-behavior)
        * [loc]
            (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)
            (https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values)
        * [iloc]
            (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html)
            (https://stackoverflow.com/questions/14941097/selecting-pandas-column-by-location)
        * [Remove Columns](https://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe)
            del
                del df['column_name']
                del df.column_name
            drop
                df.drop(columns=['coleta', 'MM'])
                df.drop(['coleta', 'MM'], axis=1, inplace=True)
        * [Dataframe to CSV](https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file)
    '''
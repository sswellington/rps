import csv
import numpy as np
import pandas as pd


class Season(object):
    ''' Docs and Reference 
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
    
    def __init__(self, path):
        self._df = pd.read_csv(path) 
        
    
    def set_dataframe(self, path):
        self._df = pd.read_csv(path) 
    
    
    def get_dataframe(self):
        return self._df
    
    
    def len_columns(self):
        return len(self._df.columns)
    
    
    def info(self):
        return self._df.info()    
    
    
    def shape(self):
        return self._df.shape
        
        
    def query_avg_per_year(self, year):
        df = self._df.loc[self._df['YYYY'] == year]
        
        df = np.array(df, dtype=float)
        df = pd.DataFrame(df)
        df = (df.mean())
        
        swap = []
        for i in df:
            swap.append(i)
        return swap
    
    
    def split(self, season):
        df = self._df.loc[self._df['class'] == season]
        del df['class']
        self.dataframe_2_csv(df, ('database/split/'+season.lower()+'.csv'))
    
    
    def avg(self, season, year, period_in_year):
        del self._df['MM']
        del self._df['coleta']
        this = pd.DataFrame(self._df.iloc[[0]]) # set header of dataframe
        
        for x in range(period_in_year):
            this.loc[x] = self.query_avg_per_year(year)      
            year += 1     
        self.dataframe_2_csv(this, ('database/avg/'+season.lower()+'.csv'))
      
        
    def dataframe_2_csv(self, dataframe, path):
        dataframe.to_csv(path, encoding='utf-8', index=False)  
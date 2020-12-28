import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
        self._path = path
    
        
    def query_avg_per_year(self, dataframe, year):
        df = dataframe.loc[dataframe['YYYY'] == year]
        df = np.array(df, dtype=float)
        df = pd.DataFrame(df)
        df = (df.mean())
        swap = []
        for i in df:
            swap.append(i)
        return swap
    
    
    def split(self, df, season):
        df = df.loc[df['estação'] == season]
        del df['estação']
        df.to_csv(self._path+'split/'+season.lower()+'.csv', encoding='utf-8', index=False)
    
    
    def avg(self, df, season, year):
        del df['MM']
        del df['coleta']
        this = pd.DataFrame(df.iloc[[0]]) # set header of dataframe
        
        for x in range(25):
            this.loc[x] = self.query_avg_per_year(df,year)      
            year += 1     
        
        this.to_csv(self._path+'avg/'+season.lower()+'.csv', encoding='utf-8', index=False)
    
        
    def plot(self, x, y, title, unit):
        plt.plot(x, y[0], label = "Verão", color="r", marker=".")
        plt.plot(x, y[1], label = "Outono", color="darkorange", marker=".")
        plt.plot(x, y[2], label = "Inverno", color="b", marker=".")
        plt.plot(x, y[3], label = "Primavera", color="g", marker=".")
        plt.grid()
        
        plt.title(title+" do Rio Paraíba do Sul")
        plt.xlabel("Anos")
        plt.ylabel(title+' ('+ unit+')')
        plt.legend()
        plt.savefig('view/'+title+'.pdf', dpi=300) 
        plt.cla()   # Clear axis
        plt.clf()   # Clear figure
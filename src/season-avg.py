import csv
import numpy as np
import pandas as pd

from Log import *

PATH = 'database/'


def query_avg_per_year(dataframe, year):
    df = dataframe.loc[dataframe['YYYY'] == year]
    df = np.array(df, dtype=float)
    df = pd.DataFrame(df)
    df = (df.mean())
    swap = []
    for i in df:
        swap.append(i)
    return swap


def avg(df, season, year):
    del df['MM']
    del df['coleta']
    this = pd.DataFrame(df.iloc[[0]]) # set header of dataframe
    
    for x in range(25):
        this.loc[x] = query_avg_per_year(df,year)      
        year += 1     
    
    this.to_csv(PATH+'avg/'+season.lower()+'.csv', encoding='utf-8', index=False)


if __name__ == "__main__" :
    l = Log()
    tp_season = ('V','O','I','P')
    
    for s in tp_season: 
        year = 1995
        df = pd.read_csv(PATH+'split/'+s.lower()+'.csv')
        avg(df, s, year)
    
    l.time('avg')
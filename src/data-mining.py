import csv
import numpy as np
import pandas as pd

if __name__ == "__main__" :
    tp_season = ('V','O','I','P')
    df = pd.read_csv('database/source.csv')
    
    df.info()
    
    
    year = 1995
    nine = df[(df['YYYY'] == year) & (df['class']!= 'V')]
    
    nine.info()
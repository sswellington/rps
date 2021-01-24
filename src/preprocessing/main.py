from pandas import read_csv as pd_read_csv

from library import Preprocessing


if __name__ == "__main__" :
    PATH = 'database/source.csv'
    LABEL = ('V','O','I','P')
    STARTING_YEAR = 1995
    FINAL_YEAR = 2019
    
    df = pd_read_csv(PATH)
    rps = Preprocessing(df)
    del df
    
    rps.export(LABEL, 'database/preprocessing.csv')
    del rps
    
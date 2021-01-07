import pandas as pd

from library.Preprocessing import Preprocessing


PATH = 'database/source.csv'
LABEL = ('V','O','I','P')
STARTING_YEAR = 1995
FINAL_YEAR = 2019


if __name__ == "__main__" :
    
    df = pd.read_csv(PATH)
    rps = Preprocessing(df)
    del df
    
    rps.export(LABEL, 'database/preprocessing.csv')
    del rps

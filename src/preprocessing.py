import pandas as pd

from library.Preprocessing import Preprocessing

PATH = 'database/source.csv'
LABEL = ('V','O','I','P')


if __name__ == "__main__" :
    df = pd.read_csv(PATH)
     
    rps = Preprocessing(df, 1995, 2019)
    rps.export(LABEL, 'database/clean.csv')
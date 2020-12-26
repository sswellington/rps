import csv
import pandas as pd

from Log import *

PATH = 'database/'


def split(df, season):
    """ Docs and Reference 
        * [loc]
            (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)
            (https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values)
        * [Remove Columns](https://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe)
            del
                del df['column_name']
                del df.column_name
            drop
                df.drop(columns=['coleta', 'MM'])
                df.drop(['coleta', 'MM'], axis=1, inplace=True)
        * [Dataframe to CSV](https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file)
    """
    df = df.loc[df['estação'] == season]
    del df['estação']
    df.to_csv(PATH+'split/'+season.lower()+'.csv', encoding='utf-8', index=False)
    

if __name__ == "__main__" :
    ''' Meteorological Seasons in the southern hemisphere (adapted for upward approach (ceil))
        * Summer: January - March
        * Fall (autumn): April - June
        * Winter: July - September
        * Spring: October - December

        Refences
            [USP](https://www.iag.usp.br/astronomia/inicio-das-estacoes-do-ano)
            [Fiocruz](http://www.fiocruz.br/biosseguranca/Bis/infantil/estacoes-ano.htm#:~:text=Todo%20mundo%20j%C3%A1%20sabe%20que,do%20sol%2C%20dura%20um%20ano.)
    '''
    l = Log()
    tp_season = ('V','O','I','P')
    dataframe = pd.read_csv(PATH+'rps.csv')
    
    for s in tp_season: 
        split(dataframe,s)
        
    l.time('split')
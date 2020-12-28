import csv
import pandas as pd

from Log import *

PATH = 'database/'


def split(df, season):
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
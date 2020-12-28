from Log import *
from Season import *


# clean the data
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
    PATH = 'database/'
    season = Season(PATH)
    tp_season = ('V','O','I','P')
    
    
    ''' SPLIT ''' 
    dataframe = pd.read_csv(PATH+'rps.csv')   
    for s in tp_season: 
        season.split(dataframe,s)
    
    
    ''' AVG '''
    for s in tp_season: 
        year = 1995
        df = pd.read_csv(PATH+'split/'+s.lower()+'.csv')
        season.avg(df, s, year)
    
    l.time('season')
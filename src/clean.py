from library.Log import Log
from library.Season import Season


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
    tp_season = ('V','O','I','P')
    season = Season('database/rps.csv')
    
    
    ''' SPLIT ''' 
    for s in tp_season: 
        season.split(s)
    
    
    ''' AVG '''
    for s in tp_season: 
        year = 1995
        season.set_dataframe('database/split/'+s.lower()+'.csv')
        season.avg(s, year, 25)
    
    l.time('season')
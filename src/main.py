from Log import *
from Season import *

PATH = 'database/'


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
    season = Season(PATH)
    tp_season = ('V','O','I','P')
    
    
    ''' SPLIT ''' 
    # dataframe = pd.read_csv(PATH+'rps.csv')   
    # for s in tp_season: 
    #     season.split(dataframe,s)
    
    
    ''' AVG '''
    # for s in tp_season: 
    #     year = 1995
    #     df = pd.read_csv(PATH+'split/'+s.lower()+'.csv')
    #     season.avg(df, s, year)
    
    
    ''' VIEW '''
    title = ('Vazão','Temperatura','pH','Condutividade','OD',
             'HCO3','MPS','Clorofila','COD',
             'NO2','NO3','NH4','NID','NT','NTD','NOD',
             'NP','PO4','PTD','PT','POD', 'PP ','Silica',
             'Cl','SO','Na','Ca','K','Mg')
    unit = ('m³/s','ºC','','µS/cm','mg/L',
            'meq/L','mg/L','mg/L','mg/L',
            'µM','µM','µM','µM','µM','µM','µM',
            'µM','µM','µM','µM','µM', 'µM','µM',
            'mg/L','mg/L','mg/L','mg/L','mg/L','mg/L')
    
    df_v = pd.read_csv(PATH+'avg/'+tp_season[0].lower()+'.csv')
    df_o = pd.read_csv(PATH+'avg/'+tp_season[1].lower()+'.csv')
    df_i = pd.read_csv(PATH+'avg/'+tp_season[2].lower()+'.csv')
    df_p = pd.read_csv(PATH+'avg/'+tp_season[3].lower()+'.csv')
    
    x = df_v.iloc[:, 0]
    
    for i in range(len(title)):
        y = []
        y.append(df_v.iloc[:, i+1])
        y.append(df_o.iloc[:, i+1])
        y.append(df_i.iloc[:, i+1])
        y.append(df_p.iloc[:, i+1])
        season.plot(x, y, title[i], unit[i])
        
    l.time('season')